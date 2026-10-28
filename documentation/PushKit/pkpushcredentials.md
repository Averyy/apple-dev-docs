# PKPushCredentials

**Framework**: PushKit  
**Kind**: class  
**Role**: Class

An object that encapsulates the device token you use to deliver push notifications to your app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class PKPushCredentials
```

```objc
@interface PKPushCredentials : NSObject
```

## Mentions

- [Supporting PushKit Notifications in Your App](./supporting-pushkit-notifications-in-your-app.md)

## Overview

When registering your app’s push types, PushKit creates a `PKPushCredentials` object for each type your app supports and delivers it to your delegate’s [`pushRegistry(_:didUpdate:for:)`](./pkpushregistrydelegate/pushregistry%28_,didupdate,for%29.md) method. Don’t create `PKPushCredentials` objects yourself.

## Topics

### Getting the Token
- [var token: Data](./pkpushcredentials/token.md)
  A unique device token to use when sending push notifications to the current device.
- [var type: PKPushType](./pkpushcredentials/type.md)
  The push type constant associated with the token.

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

### Registration
- [Supporting PushKit Notifications in Your App](./supporting-pushkit-notifications-in-your-app.md)
  Declare the types of PushKit notifications your app supports and configure objects to respond to them.
- [class PKPushRegistry](./pkpushregistry.md)
  An object that requests the delivery and handles the receipt of PushKit notifications.
- [protocol PKPushRegistryDelegate](./pkpushregistrydelegate.md)
  The methods that you use to handle incoming PushKit notifications and registration events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushkit/pkpushcredentials)*