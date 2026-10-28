# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an environment property to read an observable object from the environment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ objectType: Value.Type) where Value : AnyObject, Value : Observable
```

**Other overloads**:

```swift
init(_ keyPath: KeyPath<EnvironmentValues, Value>)
```

```swift
init<T>(_ objectType: T.Type) where Value == T?, T : AnyObject, T : Observable
```

## Discussion

> ❗ **Important**: This initializer only accepts objects conforming to the `Observable` protocol. For reading environment objects that conform to `ObservableObject`, use [`EnvironmentObject`](../environmentobject.md) instead.

Don’t call this initializer directly. Instead, declare a property with the [`Environment`](../environment.md) property wrapper, passing the object’s type to the wrapper (using this syntax, the object type can be omitted from the end of property declaration):

```swift
@Observable final class Profile { ... }

struct MyView: View {
    @Environment(Profile.self) private var currentProfile

    // ...
}
```

> ⚠️ **Warning**: If no object has been set in the view’s environment, this property will issue a fatal error when accessed. To safely check for the existence of an environment object, initialize the environment property with an optional object type instead.

SwiftUI automatically updates any parts of `MyView` that depend on the property when the associated environment object changes.

You can’t modify the environment object using a property like this. Instead, use the [`environment(_:)`](../view/environment%28_%29.md) view modifier on a view to set an object for a view hierarchy.

## Parameters

- `objectType`: The type of the `Observable` object to read from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environment/init(_:)-7pint)*