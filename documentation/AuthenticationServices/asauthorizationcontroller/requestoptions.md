# ASAuthorizationController.RequestOptions

**Framework**: Authentication Services  
**Kind**: struct

Options that modify how a controller performs authorization requests.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct RequestOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](asauthorizationcontroller/requestoptions/init(rawvalue:).md)
### Constants
- [static var preferImmediatelyAvailableCredentials: ASAuthorizationController.RequestOptions](asauthorizationcontroller/requestoptions/preferimmediatelyavailablecredentials.md)
  Tells the authorization controller to prefer credentials that are immediately available on the local device.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func performRequests()](asauthorizationcontroller/performrequests.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](asauthorizationcontroller/performrequests(options:).md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](asauthorizationcontroller/performautofillassistedrequests.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](asauthorizationcontroller/cancel.md)
  Cancels any active authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/requestoptions)*