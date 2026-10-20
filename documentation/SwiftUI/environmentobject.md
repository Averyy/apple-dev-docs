# EnvironmentObject

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

An environment object invalidates the current view whenever the observable object that conforms to [`ObservableObject`](../Combine/observableobject.md) changes. If you declare a property as an environment object, be sure to set a corresponding model object on an ancestor view by calling its [`environmentObject(_:)`](./view/environmentobject%28_%29.md) modifier.

> **Note**: If your observable object conforms to the [`Observable`](../Observation/observable.md) protocol, use [`Environment`](./environment.md) instead of `EnvironmentObject` and set the model object in an ancestor view by calling its [`environment(_:)`](./view/environment%28_%29.md) or [`environment(_:_:)`](./view/environment%28_,_%29.md) modifiers.

## Topics

### Creating an environment object
- [init()](./environmentobject/init%28%29.md)
  Creates an environment object.
### Getting the value
- [var wrappedValue: ObjectType](./environmentobject/wrappedvalue.md)
  The underlying value referenced by the environment object.
- [var projectedValue: EnvironmentObject<ObjectType>.Wrapper](./environmentobject/projectedvalue.md)
  A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [EnvironmentObject.Wrapper](./environmentobject/wrapper.md)
  A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

## Relationships

### Conforms To
- [DynamicProperty](./dynamicproperty.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Distributing model data throughout your app
- [func environmentObject<T>(T) -> some View](./view/environmentobject%28_%29.md)
  Supplies an observable object to a view’s hierarchy.
- [func environmentObject<T>(T) -> some Scene](./scene/environmentobject%28_%29.md)
  Supplies an `ObservableObject` to a view subhierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject)*