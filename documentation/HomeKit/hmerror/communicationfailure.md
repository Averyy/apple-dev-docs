# communicationFailure

**Framework**: HomeKit  
**Kind**: property

A communication failure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var communicationFailure: HMError.Code { get }
```

## See Also

- [static var accessDenied: HMError.Code](hmerror/accessdenied.md)
  An error indicating the current user doesn’t have privileges to perform the operation.
- [static var accessoryCommunicationFailure: HMError.Code](hmerror/accessorycommunicationfailure.md)
  The accessory failed to communicate.
- [static var accessoryPairingFailed: HMError.Code](hmerror/accessorypairingfailed.md)
  An attempt to pair with the accessory has failed.
- [static var accessorySentInvalidResponse: HMError.Code](hmerror/accessorysentinvalidresponse.md)
  An error indicating the accessory sent an invalid response.
- [static var clientRequestError: HMError.Code](hmerror/clientrequesterror.md)
  An error with the client request.
- [static var dataResetFailure: HMError.Code](hmerror/dataresetfailure.md)
  An attempt to reset the data failed.
- [static var timedOutWaitingForAccessory: HMError.Code](hmerror/timedoutwaitingforaccessory.md)
  An accessory did not respond timely.
- [static var partialCommunicationFailure: HMError.Code](hmerror/partialcommunicationfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/communicationfailure)*