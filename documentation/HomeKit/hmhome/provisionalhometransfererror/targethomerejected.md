# HMHome.ProvisionalHomeTransferError.targetHomeRejected

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

The home hub rejected the target home identifier.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
case targetHomeRejected
```

## Overview

A home hub rejects a request to transfer a home if the provided home identifier doesn’t match it or HomeKit can’t create a snapshot of the home it tries to transfer.

## See Also

### Detecting transfer errors
- [HMHome.ProvisionalHomeTransferError.authenticationFailed](./authenticationfailed.md)
  Authentication with the home hub failed.
- [HMHome.ProvisionalHomeTransferError.connectionFailed](./connectionfailed.md)
  Establishing a network connection to the home hub failed.
- [HMHome.ProvisionalHomeTransferError.serverError](./servererror.md)
  An unexpected server-side error or internal error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransfererror/targethomerejected)*