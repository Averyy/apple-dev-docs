# AccessibilityFocusState.Binding

**Framework**: SwiftUI  
**Kind**: struct

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
@propertyWrapper
@frozen struct Binding
```

## Topics

### Getting the state
- [var projectedValue: AccessibilityFocusState<Value>.Binding](accessibilityfocusstate/binding/projectedvalue.md)
  The currently focused element.
- [var wrappedValue: Value](accessibilityfocusstate/binding/wrappedvalue.md)
  The underlying value referenced by the bound property.

## See Also

- [var projectedValue: AccessibilityFocusState<Value>.Binding](accessibilityfocusstate/projectedvalue.md)
  A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.
- [var wrappedValue: Value](accessibilityfocusstate/wrappedvalue.md)
  The current state value, taking into account whatever bindings might be in effect due to the current location of focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/binding)*