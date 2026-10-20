# partialCommunicationFailure

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static var partialCommunicationFailure: HMError.Code { get }
```

## See Also

### Detecting communication errors
- [static var accessDenied: HMError.Code](./accessdenied.md)
  An error indicating the current user doesn’t have privileges to perform the operation.
- [static var accessoryCommunicationFailure: HMError.Code](./accessorycommunicationfailure.md)
  The accessory failed to communicate.
- [static var accessoryPairingFailed: HMError.Code](./accessorypairingfailed.md)
  An attempt to pair with the accessory has failed.
- [static var accessorySentInvalidResponse: HMError.Code](./accessorysentinvalidresponse.md)
  An error indicating the accessory sent an invalid response.
- [static var clientRequestError: HMError.Code](./clientrequesterror.md)
  An error with the client request.
- [static var communicationFailure: HMError.Code](./communicationfailure.md)
  A communication failure.
- [static var dataResetFailure: HMError.Code](./dataresetfailure.md)
  An attempt to reset the data failed.
- [static var timedOutWaitingForAccessory: HMError.Code](./timedoutwaitingforaccessory.md)
  An accessory did not respond timely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/partialcommunicationfailure)*