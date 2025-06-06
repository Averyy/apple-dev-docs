# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The underlying value referenced by the environment object.

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
@preconcurrency var wrappedValue: ObjectType { get }
```

#### Discussion

This property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you use the property variable created with the [`EnvironmentObject`](environmentobject.md) attribute.

When a mutable value changes, the new value is immediately available. However, a view displaying the value is updated asynchronously and may not show the new value immediately.

## See Also

- [var projectedValue: EnvironmentObject<ObjectType>.Wrapper](environmentobject/projectedvalue.md)
  A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [EnvironmentObject.Wrapper](environmentobject/wrapper.md)
  A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject/wrappedvalue)*