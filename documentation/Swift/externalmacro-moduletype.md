# externalMacro(module:type:)

**Framework**: Swift  
**Kind**: macro

Specifies the module and type name for a macro’s implementation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@freestanding
(expression) macro externalMacro<T>(module: String, type: String) -> T
```

#### Return Value

The macro’s implementation.

#### Overview

This macro can only be used to define a macro; using it in any other context is an error. The specified type must conform to the protocols that correspond to the roles of the macro being declared. For example:

```swift
macro stringify(_ value: T) -> (T, String) =
    #externalMacro(module: "ExampleMacros", type: "StringifyMacro")
```

## Parameters

- `module`: The module name.
- `type`: The type that implements the macro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/externalmacro(module:type:))*