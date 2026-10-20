# projectedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

Use `projectedValue` in conjunction with [`accessibilityFocused(_:equals:)`](../view/accessibilityfocused%28_,equals%29.md) to establish bindings between view content and accessibility focus placement.

## See Also

### Getting the state
- [var wrappedValue: Value](./wrappedvalue.md)
  The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
- [AccessibilityFocusState.Binding](./binding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/projectedvalue)*