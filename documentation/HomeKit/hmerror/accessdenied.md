# accessDenied

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An error indicating the current user doesn’t have privileges to perform the operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var accessDenied: HMError.Code { get }
```

## See Also

### Detecting communication errors
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
- [static var partialCommunicationFailure: HMError.Code](./partialcommunicationfailure.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/accessdenied)*