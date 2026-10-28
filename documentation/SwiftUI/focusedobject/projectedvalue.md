# projectedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A projection of the focused object that creates bindings to its properties using dynamic member lookup.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency var projectedValue: FocusedObject<ObjectType>.Wrapper? { get }
```

## Discussion

Use the projected value to pass a focused object down a view hierarchy.

## See Also

### Getting the value
- [var wrappedValue: ObjectType?](./wrappedvalue.md)
  The underlying value referenced by the focused object.
- [FocusedObject.Wrapper](./wrapper.md)
  A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedobject/projectedvalue)*