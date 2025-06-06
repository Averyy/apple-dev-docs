# grantCapability(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Grants the specified capability to the process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func grantCapability(_ capability: ProcessCapability) throws -> ProcessCapability.Grant
```

#### Return Value

A [`ProcessCapability.Grant`](processcapability/grant.md) object that represents the granted capability.

#### Overview

When the process no longer needs the capability, call [`invalidate()`](processcapability/grant/invalidate().md) on the returned object.

## Parameters

- `capability`: The capability to grant.

## See Also

- [func grantCapability(ProcessCapability, invalidationHandler: () -> Void) throws -> ProcessCapability.Grant](networkingprocess/grantcapability(_:invalidationhandler:).md)
  Grants the specified capability to the process, calling the handler when the capability becomes invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess/grantcapability(_:))*