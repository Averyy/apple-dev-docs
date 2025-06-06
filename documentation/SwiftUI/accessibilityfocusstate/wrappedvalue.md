# wrappedValue

**Framework**: SwiftUI  
**Kind**: property

The current state value, taking into account whatever bindings might be in effect due to the current location of focus.

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
var wrappedValue: Value { get nonmutating set }
```

#### Discussion

When focus is not in any view that is bound to this state, the wrapped value will be `nil` (for optional-typed state) or `false` (for `Bool`- typed state).

## See Also

- [var projectedValue: AccessibilityFocusState<Value>.Binding](accessibilityfocusstate/projectedvalue.md)
  A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.
- [AccessibilityFocusState.Binding](accessibilityfocusstate/binding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/wrappedvalue)*