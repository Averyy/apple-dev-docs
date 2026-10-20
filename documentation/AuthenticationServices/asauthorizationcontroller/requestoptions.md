# ASAuthorizationController.RequestOptions

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

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

```c
enum ASAuthorizationControllerRequestOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./requestoptions/init%28rawvalue%29.md)
### Constants
- [static var preferImmediatelyAvailableCredentials: ASAuthorizationController.RequestOptions](./requestoptions/preferimmediatelyavailablecredentials.md)
  Tells the authorization controller to prefer credentials that are immediately available on the local device.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Executing requests
- [func performRequests()](./performrequests%28%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performRequests(options: ASAuthorizationController.RequestOptions)](./performrequests%28options%29.md)
  Starts the specified authorization flows during controller initialization.
- [func performAutoFillAssistedRequests()](./performautofillassistedrequests%28%29.md)
  Initiates the authorization flows for requests that support AutoFill presentation.
- [func cancel()](./cancel%28%29.md)
  Cancels any active authorization requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/requestoptions)*