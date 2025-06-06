# FocusState.Binding

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that can read and write a value that indicates the current focus location.

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
@frozen
@propertyWrapper struct Binding
```

## Topics

### Inspecting the binding
- [var projectedValue: FocusState<Value>.Binding](focusstate/binding/projectedvalue.md)
  A projection of the binding value that returns a binding.
- [var wrappedValue: Value](focusstate/binding/wrappedvalue.md)
  The underlying value referenced by the bound property.

## See Also

- [var projectedValue: FocusState<Value>.Binding](focusstate/projectedvalue.md)
  A projection of the focus state value that returns a binding.
- [var wrappedValue: Value](focusstate/wrappedvalue.md)
  The current state value, taking into account whatever bindings might be in effect due to the current location of focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusstate/binding)*