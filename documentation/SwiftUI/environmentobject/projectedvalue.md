# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the environment object that creates bindings to its properties using dynamic member lookup.

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
@preconcurrency var projectedValue: EnvironmentObject<ObjectType>.Wrapper { get }
```

#### Discussion

Use the projected value to pass an environment object down a view hierarchy.

## See Also

- [var wrappedValue: ObjectType](environmentobject/wrappedvalue.md)
  The underlying value referenced by the environment object.
- [EnvironmentObject.Wrapper](environmentobject/wrapper.md)
  A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject/projectedvalue)*