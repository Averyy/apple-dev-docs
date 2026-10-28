# HMHome.ProvisionalHomeTransferError.authenticationFailed

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

Authentication with the home hub failed.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case authenticationFailed
```

## Overview

Typical causes for authentication failures with a home hub include an invalid or expired transfer token, a failure during a `TLS` or `mTLS` handshake, and mismatching credentials.

## See Also

### Detecting transfer errors
- [HMHome.ProvisionalHomeTransferError.connectionFailed](./connectionfailed.md)
  Establishing a network connection to the home hub failed.
- [HMHome.ProvisionalHomeTransferError.serverError](./servererror.md)
  An unexpected server-side error or internal error occurred.
- [HMHome.ProvisionalHomeTransferError.targetHomeRejected](./targethomerejected.md)
  The home hub rejected the target home identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransfererror/authenticationfailed)*