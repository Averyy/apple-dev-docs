# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the binding value that returns a binding.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var projectedValue: FocusState<Value>.Binding { get }
```

#### Discussion

Use the projected value to pass a binding value down a view hierarchy.

## See Also

- [var wrappedValue: Value](focusstate/binding/wrappedvalue.md)
  The underlying value referenced by the bound property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusstate/binding/projectedvalue)*