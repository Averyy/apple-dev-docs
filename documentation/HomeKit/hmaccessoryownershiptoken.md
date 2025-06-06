# HMAccessoryOwnershipToken

**Framework**: HomeKit  
**Kind**: class

Authentication data that your app provides when adding an accessory to a home.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class HMAccessoryOwnershipToken
```

#### Overview

If you manufacture an accessory that requires user authentication to add the accessory to a home, manage the authentication in your app and produce a token that represents the successful outcome of that process. Wrap the token data in an [`HMAccessoryOwnershipToken`](hmaccessoryownershiptoken.md) instance and call the [`init(url:ownershipToken:)`](hmaccessorysetuppayload/init(url:ownershiptoken:).md) method to create an authenticated [`HMAccessorySetupPayload`](hmaccessorysetuppayload.md) instance. Then call the [`addAndSetupAccessories(with:completionHandler:)`](hmhome/addandsetupaccessories(with:completionhandler:).md) method with the payload.

If the user attempts from the Home app to add an accessory that requires a token, the Home app calls the associated app’s [`homeManager(_:didReceiveAddAccessoryRequest:)`](hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:).md) home manager delegate method to perform the negotiation and provide the token.

## Topics

### Creating a Token
- [init?(data: Data)](hmaccessoryownershiptoken/init(data:).md)
  Creates an ownership token from data.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(url: URL?)](hmaccessorysetuppayload/init(url:).md)
  Creates an accessory setup payload.
- [init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)](hmaccessorysetuppayload/init(url:ownershiptoken:).md)
  Creates an accessory setup payload instance that includes an ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryownershiptoken)*