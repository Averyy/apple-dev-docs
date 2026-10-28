# HMAccessoryOwnershipToken

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

Authentication data that your app provides when adding an accessory to a home.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 27.0+
- visionOS 1.0+

## Declaration

```swift
class HMAccessoryOwnershipToken
```

```objc
@interface HMAccessoryOwnershipToken : NSObject
```

## Overview

If you manufacture an accessory that requires user authentication to add the accessory to a home, manage the authentication in your app and produce a token that represents the successful outcome of that process. Wrap the token data in an [`HMAccessoryOwnershipToken`](./hmaccessoryownershiptoken.md) instance and call the [`init(url:ownershipToken:)`](./hmaccessorysetuppayload/init%28url,ownershiptoken%29-32mrj.md) method to create an authenticated [`HMAccessorySetupPayload`](./hmaccessorysetuppayload.md) instance. Then call the [`addAndSetupAccessories(with:completionHandler:)`](./hmhome/addandsetupaccessories%28with,completionhandler%29.md) method with the payload.

If the user attempts from the Home app to add an accessory that requires a token, the Home app calls the associated app’s [`homeManager(_:didReceiveAddAccessoryRequest:)`](./hmhomemanagerdelegate/homemanager%28_,didreceiveaddaccessoryrequest%29.md) home manager delegate method to perform the negotiation and provide the token.

## Topics

### Creating a Token
- [init?(data: Data)](./hmaccessoryownershiptoken/init%28data%29.md)
  Creates an ownership token from data.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Payload
- [init?(url: URL?)](./hmaccessorysetuppayload/init%28url%29-7ytm5.md)
  Creates an accessory setup payload.
- [init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)](./hmaccessorysetuppayload/init%28url,ownershiptoken%29-32mrj.md)
  Creates an accessory setup payload instance that includes an ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryownershiptoken)*