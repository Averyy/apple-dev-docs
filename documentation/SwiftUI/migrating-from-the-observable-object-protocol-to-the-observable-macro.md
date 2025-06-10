# Migrating from the Observable Object protocol to the Observable macro

**Framework**: SwiftUI

Update your existing app to leverage the benefits of Observation in Swift.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- Xcode 15.0+

#### Overview

Starting with iOS 17, iPadOS 17, macOS 14, tvOS 17, and watchOS 10, SwiftUI provides support for [`Observation`](https://developer.apple.com/documentation/Observation), a Swift-specific implementation of the observer design pattern. Adopting Observation provides your app with the following benefits:

- Tracking optionals and collections of objects, which isn’t possible when using [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject).
- Using existing data flow primitives like [`State`](state.md) and [`Environment`](environment.md) instead of object-based equivalents such as [`StateObject`](stateobject.md) and [`EnvironmentObject`](environmentobject.md).
- Updating views based on changes to the observable properties that a view’s [`body`](view/body-8kl5o.md) reads instead of any property changes that occur to an observable object, which can help improve your app’s performance.

To take advantage of these benefits in your app, you’ll discover how to replace existing source code that relies on [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) with code that leverages the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro.

> **Note**: Download this sample to see the migrated version of the sample app. To see the premigrated version, download the sample available in [`Monitoring data changes in your app`](monitoring-model-data-changes-in-your-app.md). You can also use the premigrated version to code along with this article.

##### Use the Observable Macro

To adopt [`Observation`](https://developer.apple.com/documentation/Observation) in an existing app, begin by replacing [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) in your data model type with the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro. The [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro generates source code at compile time that adds observation support to the type.

Then remove the [`Published`](https://developer.apple.com/documentation/Combine/Published) property wrapper from observable properties. Observation doesn’t require a property wrapper to make a property observable. Instead, the accessibility of the property in relationship to an observer, such as a view, determines whether a property is observable.

If you have properties that are accessible to an observer that you don’t want to track, apply the [`ObservationIgnored()`](https://developer.apple.com/documentation/Observation/ObservationIgnored()) macro to the property.

##### Migrate Incrementally

You don’t need to make a wholesale replacement of the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol throughout your app. Instead, you can make changes incrementally. Start by changing one data model type to use the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro. Your app can mix data model types that use different observation systems. However, SwiftUI tracks changes differently based on the observation system that a data model type uses, `Observable` versus `ObservableObject`.

You may notice slight behavioral differences in your app based on the tracking method. For instance, when tracking as [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()), SwiftUI updates a view only when an observable property changes and the view’s [`body`](view/body-8kl5o.md) reads the property directly. The view doesn’t update when observable properties not read by `body` changes. In contrast, a view updates when any published property of an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) instance changes, even if the view doesn’t read the property that changes, when tracking as `ObservableObject`.

> **Note**: To learn more about when SwiftUI updates views when observable properties change, see [`Managing model data in your app`](managing-model-data-in-your-app.md).

##### Migrate Other Source Code

The only change made to the sample app so far is to apply the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro to `Library` and remove support for the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol. The app still uses the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) data flow primitive like [`StateObject`](stateobject.md) to manage an instance of `Library`. If you were to build and run the app, SwiftUI still updates the views as expected. That’s because data flow property wrappers such as [`StateObject`](stateobject.md) and [`EnvironmentObject`](environmentobject.md) support types that use the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro. SwiftUI provides this support so apps can make source code changes incrementally.

However, to fully adopt [`Observation`](https://developer.apple.com/documentation/Observation), replace the use of [`StateObject`](stateobject.md) with [`State`](state.md) after updating your data model type. For example, in the following code the main app structure creates an instance of `Library` and stores it as a `StateObject`. It also adds the `Library` instance to the environment using the [`environmentObject(_:)`](view/environmentobject(_:).md) modifier.

```swift
// BEFORE
@main
struct BookReaderApp: App {
    @StateObject private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environmentObject(library)
        }
    }
}
```

Now that `Library` no longer conforms to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject), the code can change to use [`State`](state.md) instead of [`StateObject`](stateobject.md) and to add `library` to the environment using the [`environment(_:)`](view/environment(_:).md) modifier.

```swift
// AFTER
@main
struct BookReaderApp: App {
    @State private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(library)
        }
    }
}
```

One more change must happen before `Library` fully adopts [`Observation`](https://developer.apple.com/documentation/Observation). Previously the view `LibraryView` retrieved a `Library` instance from the environment using the [`EnvironmentObject`](environmentobject.md) property wrapper. The new code, however, uses the [`Environment`](environment.md) property wrapper instead.

##### Remove the Observedobject Property Wrapper

To wrap up the migration of the sample app, change the data model type `Book` to support [`Observation`](https://developer.apple.com/documentation/Observation) by removing [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) from the type declaration and apply the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro. Then remove the [`Published`](https://developer.apple.com/documentation/Combine/Published) property wrapper from observable properties.

Next, remove the [`ObservedObject`](observedobject.md) property wrapper from the `book` variable in the `BookView`. This property wrapper isn’t needed when adopting [`Observation`](https://developer.apple.com/documentation/Observation). That’s because SwiftUI automatically tracks any observable properties that a view’s [`body`](view/body-8kl5o.md) reads directly. For example, SwiftUI updates `BookView` when `book.title` changes.

However, if a view needs a binding to an observable type, replace [`ObservedObject`](observedobject.md) with the [`Bindable`](bindable.md) property wrapper. This property wrapper provides binding support to an observable type so that views that expect a binding can change an observable property. For instance, in the following code [`TextField`](textfield.md) receives a binding to `book.title`:

## See Also

- [Managing model data in your app](managing-model-data-in-your-app.md)
  Create connections between your app’s data model and views.
- [@attached(member, names: named(_$observationRegistrar), named(access), named(withMutation), named(shouldNotifyObservers)) @attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()](../Observation/Observable().md)
  Defines and implements conformance of the Observable protocol.
- [Monitoring data changes in your app](monitoring-model-data-changes-in-your-app.md)
  Show changes to data in your app’s user interface by using observable objects.
- [struct StateObject](stateobject.md)
  A property wrapper type that instantiates an observable object.
- [struct ObservedObject](observedobject.md)
  A property wrapper type that subscribes to an observable object and invalidates a view whenever the observable object changes.
- [protocol ObservableObject : AnyObject](../Combine/ObservableObject.md)
  A type of object with a publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro)*