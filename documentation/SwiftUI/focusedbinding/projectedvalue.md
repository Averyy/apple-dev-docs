# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A binding to the optional value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var projectedValue: Binding<Value?> { get }
```

#### Discussion

The unwrapped value is `nil` when no focused view hierarchy has published a corresponding binding.

## See Also

- [var wrappedValue: Value?](focusedbinding/wrappedvalue.md)
  The unwrapped value for the focus key given the current scope and state of the focused view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedbinding/projectedvalue)*