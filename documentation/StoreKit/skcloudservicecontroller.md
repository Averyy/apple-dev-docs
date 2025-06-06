# SKCloudServiceController

**Framework**: StoreKit  
**Kind**: class

An object that determines the current capabilities of a person’s Music library.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
class SKCloudServiceController
```

## Mentions

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
- [Offering Apple Music Subscription in Your App](offering-apple-music-subscription-in-your-app.md)

#### Overview

Use an [`SKCloudServiceController`](skcloudservicecontroller.md) object to determine the current capabilities of a customer’s Music library, like whether the device allows playback of Apple Music catalog tracks and the addition of tracks to the library.

## Topics

### Getting authorization to access the Music library
- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)
  Prompt the customer to authorize access to Apple Music library.
- [class func authorizationStatus() -> SKCloudServiceAuthorizationStatus](skcloudservicecontroller/authorizationstatus.md)
  Returns the type of authorization the customer has for accessing the Music library on the device.
- [class func requestAuthorization((SKCloudServiceAuthorizationStatus) -> Void)](skcloudservicecontroller/requestauthorization(_:).md)
  Asks the customer for permission to access the Music library on the device.
- [enum SKCloudServiceAuthorizationStatus](skcloudserviceauthorizationstatus.md)
  Constants that indicate the type of authorization the customer has for accessing the Music library.
### Determining capabilities
- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:).md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:).md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](skcloudservicecontroller/requestcapabilities(completionhandler:).md)
  Gets the current capabilities associated with the Music library on the device.
- [struct SKCloudServiceCapability](skcloudservicecapability.md)
  Constants that specify the current capabilities of the customer’s Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontidentifier(completionhandler:).md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:).md)
### Notifications
- [static let SKStorefrontIdentifierDidChange: NSNotification.Name](../foundation/nsnotification/name/1620636-skstorefrontidentifierdidchange.md)
  A notification name for indicating a change in the storefront identifier associated with the device.
- [static let SKCloudServiceCapabilitiesDidChange: NSNotification.Name](../foundation/nsnotification/name/1620626-skcloudservicecapabilitiesdidcha.md)
  A notification name for indicating a change in the capabilities associated with the Music library on the device.
- [static let SKStorefrontCountryCodeDidChange: NSNotification.Name](../foundation/nsnotification/name/2909077-skstorefrontcountrycodedidchange.md)
  A notification name for indicating a change in the storefront country or region code associated with the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SKCloudServiceSetupViewController](skcloudservicesetupviewcontroller.md)
  A view controller that helps people perform setup for a cloud service, like an Apple Music subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecontroller)*