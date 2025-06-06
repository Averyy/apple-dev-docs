# invalidParameter

**Framework**: HomeKit  
**Kind**: property

An error indicating the object is invalid for the given operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var invalidParameter: HMError.Code { get }
```

#### Discussion

For example, the home object issues an error when attempting to add a room that exists in another home.

## See Also

- [static var missingParameter: HMError.Code](hmerror/missingparameter.md)
  An error indicating a missing parameter.
- [static var nilParameter: HMError.Code](hmerror/nilparameter.md)
  An error indicating that nil was passed for an operation that does not accept nil.
- [static var unconfiguredParameter: HMError.Code](hmerror/unconfiguredparameter.md)
  An error indicating an unconfigured parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/invalidparameter)*