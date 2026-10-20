# SKCloudServiceController

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

An object that determines the current capabilities of a person’s Music library.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use [SwiftUI](../SwiftUI/SwiftUI.md) and  [MusicKit](../MusicKit/MusicKit.md) instead.

## Declaration

```swift
class SKCloudServiceController
```

```objc
@interface SKCloudServiceController : NSObject
```

## Mentions

- [Determining a person’s Apple Music capabilities](./determining-a-person-s-apple-music-capabilities.md)
- [Requesting Access to Apple Music Library](./requesting-access-to-apple-music-library.md)
- [Offering Apple Music Subscription in Your App](./offering-apple-music-subscription-in-your-app.md)

#### Overview

Use an [`SKCloudServiceController`](./skcloudservicecontroller.md) object to determine the current capabilities of a customer’s Music library, like whether the device allows playback of Apple Music catalog tracks and the addition of tracks to the library.

## Topics

### Getting authorization to access the Music library
- [Requesting Access to Apple Music Library](./requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](./skcloudservicecontroller/authorizationstatus%28%29.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](./skcloudservicecontroller/requestauthorization%28_%29.md)
  Asks the customer for permission to access the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](./skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.
### Determining capabilities
- [Determining a person’s Apple Music capabilities](./determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requestusertoken%28fordevelopertoken,completionhandler%29.md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requeststorefrontcountrycode%28completionhandler%29.md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](./skcloudservicecontroller/requestcapabilities%28completionhandler%29.md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](./skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)
### Notifications
- [static let SKStorefrontIdentifierDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/skstorefrontidentifierdidchange.md)
  A notification name for indicating a change in the storefront identifier associated with the device.
- [static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/skcloudservicecapabilitiesdidchange.md)
  A notification name for indicating a change in the capabilities associated with the Music library on the device.
- [static let SKStorefrontCountryCodeDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/skstorefrontcountrycodedidchange.md)
  A notification name for indicating a change in the storefront country or region code associated with the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated
- [class SKCloudServiceSetupViewController](./skcloudservicesetupviewcontroller.md)
  A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller)*