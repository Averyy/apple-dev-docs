# EnvironmentObject

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type for an observable object that a parent or ancestor view supplies.

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
@frozen @propertyWrapper @preconcurrency struct EnvironmentObject<ObjectType> where ObjectType : ObservableObject
```

#### Overview

An environment object invalidates the current view whenever the observable object that conforms to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) changes. If you declare a property as an environment object, be sure to set a corresponding model object on an ancestor view by calling its [`environmentObject(_:)`](view/environmentobject(_:).md) modifier.

> **Note**: If your observable object conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol, use [`Environment`](environment.md) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [`environment(_:)`](view/environment(_:).md) or [`environment(_:_:)`](view/environment(_:_:).md) modifiers.

If your observable object conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol, use [`Environment`](environment.md) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [`environment(_:)`](view/environment(_:).md) or [`environment(_:_:)`](view/environment(_:_:).md) modifiers.

## Topics

### Creating an environment object
- [init()](environmentobject/init.md)
  Creates an environment object.
### Getting the value
- [var wrappedValue: ObjectType](environmentobject/wrappedvalue.md)
  The underlying value referenced by the environment object.
- [var projectedValue: EnvironmentObject<ObjectType>.Wrapper](environmentobject/projectedvalue.md)
  A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [EnvironmentObject.Wrapper](environmentobject/wrapper.md)
  A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func environmentObject<T>(T) -> some View](view/environmentobject(_:).md)
  Supplies an observable object to a view’s hierarchy.
- [func environmentObject<T>(T) -> some Scene](scene/environmentobject(_:).md)
  Supplies an `ObservableObject` to a view subhierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject)*