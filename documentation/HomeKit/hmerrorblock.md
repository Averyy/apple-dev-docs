# HMErrorBlock

**Framework**: HomeKit  
**Kind**: typealias

A completion block that provides an error.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias HMErrorBlock = ((any Error)?) -> Void
```

## Parameters

- `error`: The error the block returns.

## See Also

- [struct HMError](hmerror.md)
  An error HomeKit returns.
- [let HMErrorDomain: String](hmerrordomain.md)
  A string that identifies the HomeKit error domain.
- [HMError.Code](hmerror/code.md)
  Possible error values that can be returned from HomeKit APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerrorblock)*