# HMError.Code.invalidParameter

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

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
case invalidParameter
```

```c
HMErrorCodeInvalidParameter
```

#### Discussion

For example, the home object issues an error when attempting to add a room that exists in another home.

## See Also

### Parameter errors
- [HMError.Code.missingParameter](./missingparameter.md)
  An error indicating a missing parameter.
- [HMError.Code.nilParameter](./nilparameter.md)
  An error indicating that `nil` was passed for an operation that does not accept `nil`.
- [HMError.Code.unconfiguredParameter](./unconfiguredparameter.md)
  An error indicating an unconfigured parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code/invalidparameter)*