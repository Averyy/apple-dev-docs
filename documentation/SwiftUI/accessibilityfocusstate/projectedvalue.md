# projectedValue

**Framework**: SwiftUI  
**Kind**: property

A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.

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
var projectedValue: AccessibilityFocusState<Value>.Binding { get }
```

#### Discussion

Use `projectedValue` in conjunction with [`accessibilityFocused(_:equals:)`](view/accessibilityfocused(_:equals:).md) to establish bindings between view content and accessibility focus placement.

## See Also

- [var wrappedValue: Value](accessibilityfocusstate/wrappedvalue.md)
  The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
- [AccessibilityFocusState.Binding](accessibilityfocusstate/binding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/projectedvalue)*