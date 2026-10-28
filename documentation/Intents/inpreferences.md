# INPreferences

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The preferences and authorization related to using SiriKit.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPreferences
```

```objc
@interface INPreferences : NSObject
```

## Mentions

- [Requesting Authorization to Use Siri](../SiriKit/requesting-authorization-to-use-siri.md)

## Overview

Use the class methods of [`INPreferences`](./inpreferences.md) to perform tasks related to the use of SiriKit. An iOS app must request authorization to use SiriKit before Siri or Maps are allowed to call on its Intents extension to handle intents. To request authorization, call the [`requestSiriAuthorization(_:)`](./inpreferences/requestsiriauthorization%28_%29.md) method at some point during your app’s execution. The first time you call this method, the user is prompted to grant or deny authorization for your app. The user can change the authorization settings for your app later in the system settings. You can get your app’s current authorization status using the [`siriAuthorizationStatus()`](./inpreferences/siriauthorizationstatus%28%29.md) method.

## Topics

### Managing the App’s Authorization
- [class func requestSiriAuthorization((INSiriAuthorizationStatus) -> Void)](./inpreferences/requestsiriauthorization%28_%29.md)
  Requests authorization to use Siri services.
- [class func siriAuthorizationStatus() -> INSiriAuthorizationStatus](./inpreferences/siriauthorizationstatus%28%29.md)
  Returns the current authorization status of your app.
### Getting the Siri Language
- [class func siriLanguageCode() -> String](./inpreferences/sirilanguagecode%28%29.md)
  Returns the language that Siri uses to communicate with the user.

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

### Authorization
- [Requesting Authorization to Use Siri](../SiriKit/requesting-authorization-to-use-siri.md)
  Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.
- [Siri Entitlement](../BundleResources/entitlements/com.apple.developer.siri.md)
  A Boolean value that indicates whether the app handles Siri requests.
- [enum INSiriAuthorizationStatus](./insiriauthorizationstatus.md)
  Constants indicating the authorization status of your Intents extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpreferences)*