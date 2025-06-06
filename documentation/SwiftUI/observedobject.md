# ObservedObject

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that subscribes to an observable object and invalidates a view whenever the observable object changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@propertyWrapper @preconcurrency @frozen struct ObservedObject<ObjectType> where ObjectType : ObservableObject
```

#### Overview

Add the `@ObservedObject` attribute to a parameter of a SwiftUI [`View`](view.md) when the input is an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) and you want the view to update when the object’s published properties change. You typically do this to pass a [`StateObject`](stateobject.md) into a subview.

The following example defines a data model as an observable object, instantiates the model in a view as a state object, and then passes the instance to a subview as an observed object:

```swift
class DataModel: ObservableObject {
    @Published var name = "Some Name"
    @Published var isEnabled = false
}

struct MyView: View {
    @StateObject private var model = DataModel()

    var body: some View {
        Text(model.name)
        MySubView(model: model)
    }
}

struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

When any published property of the observable object changes, SwiftUI updates any view that depends on the object. Subviews can also make updates to the model properties, like the [`Toggle`](toggle.md) in the above example, that propagate to other observers throughout the view hierarchy.

Don’t specify a default or initial value for the observed object. Use the attribute only for a property that acts as an input for a view, as in the above example.

> **Note**: Don’t wrap objects conforming to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol with `@ObservedObject`. SwiftUI automatically tracks dependencies to `Observable` objects used within body and updates dependent views when their data changes. Attempting to wrap an `Observable` object with `@ObservedObject` may cause a compiler error, because it requires that its wrapped object to conform to the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol. If the view needs a binding to a property of an `Observable` object in its body, wrap the object with the [`Bindable`](bindable.md) property wrapper instead; for example, `@Bindable var model: DataModel`. For more information, see [`Managing model data in your app`](managing-model-data-in-your-app.md).

Don’t wrap objects conforming to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol with `@ObservedObject`. SwiftUI automatically tracks dependencies to `Observable` objects used within body and updates dependent views when their data changes. Attempting to wrap an `Observable` object with `@ObservedObject` may cause a compiler error, because it requires that its wrapped object to conform to the [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) protocol.

If the view needs a binding to a property of an `Observable` object in its body, wrap the object with the [`Bindable`](bindable.md) property wrapper instead; for example, `@Bindable var model: DataModel`. For more information, see [`Managing model data in your app`](managing-model-data-in-your-app.md).

## Topics

### Creating an observed object
- [init(wrappedValue: ObjectType)](observedobject/init(wrappedvalue:).md)
  Creates an observed object with an initial wrapped value.
- [init(initialValue: ObjectType)](observedobject/init(initialvalue:).md)
  Creates an observed object with an initial value.
### Getting the value
- [var wrappedValue: ObjectType](observedobject/wrappedvalue.md)
  The underlying value that the observed object references.
- [var projectedValue: ObservedObject<ObjectType>.Wrapper](observedobject/projectedvalue.md)
  A projection of the observed object that creates bindings to its properties.
- [ObservedObject.Wrapper](observedobject/wrapper.md)
  A wrapper of the underlying observable object that can create bindings to its properties.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Managing model data in your app](managing-model-data-in-your-app.md)
  Create connections between your app’s data model and views.
- [Migrating from the Observable Object protocol to the Observable macro](migrating-from-the-observable-object-protocol-to-the-observable-macro.md)
  Update your existing app to leverage the benefits of Observation in Swift.
- [@attached(member, names: named(_$observationRegistrar), named(access), named(withMutation)) @attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()](../Observation/Observable().md)
  Defines and implements conformance of the Observable protocol.
- [Monitoring data changes in your app](monitoring-model-data-changes-in-your-app.md)
  Show changes to data in your app’s user interface by using observable objects.
- [struct StateObject](stateobject.md)
  A property wrapper type that instantiates an observable object.
- [protocol ObservableObject : AnyObject](../Combine/ObservableObject.md)
  A type of object with a publisher that emits before the object has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject)*