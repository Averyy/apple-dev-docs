# missingParameter

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An error indicating a missing parameter.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var missingParameter: HMError.Code { get }
```

## See Also

### Detecting parameter errors
- [static var invalidParameter: HMError.Code](./invalidparameter.md)
  An error indicating the object is invalid for the given operation.
- [static var nilParameter: HMError.Code](./nilparameter.md)
  An error indicating that nil was passed for an operation that does not accept nil.
- [static var unconfiguredParameter: HMError.Code](./unconfiguredparameter.md)
  An error indicating an unconfigured parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/missingparameter)*