# HMAddAccessoryRequest

**Framework**: HomeKit  
**Kind**: class

A request to add an accessory to a particular home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
class HMAddAccessoryRequest
```

#### Overview

An [`HMAddAccessoryRequest`](hmaddaccessoryrequest.md) instance describes an accessory that your app should add to a home. HomeKit calls your home manager delegate’s [`homeManager(_:didReceiveAddAccessoryRequest:)`](hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:).md) method with a request.

Use the request’s [`accessoryName`](hmaddaccessoryrequest/accessoryname.md) and [`accessoryCategory`](hmaddaccessoryrequest/accessorycategory.md) properties to obtain a token by negotiating with the accessory outside of HomeKit. If the [`requiresSetupPayloadURL`](hmaddaccessoryrequest/requiressetuppayloadurl.md) property is `true`, also prepare a setup payload URL. Then create a setup payload with either the [`makePayload(url:ownershipToken:)`](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md) or [`makePayload(ownershipToken:)`](hmaddaccessoryrequest/makepayload(ownershiptoken:).md) method. Complete the request by calling the [`addAndSetupAccessories(with:completionHandler:)`](hmhome/addandsetupaccessories(with:completionhandler:).md) method on the request’s [`home`](hmaddaccessoryrequest/home.md) property.

## Topics

### Characterizing the Request
- [var home: HMHome](hmaddaccessoryrequest/home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](hmaddaccessoryrequest/accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](hmaddaccessoryrequest/accessoryname.md)
  The name of the accessory to add.
- [var requiresOwnershipToken: Bool](hmaddaccessoryrequest/requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.
- [var requiresSetupPayloadURL: Bool](hmaddaccessoryrequest/requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.
### Creating a Payload
- [func makePayload(ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?](hmaddaccessoryrequest/makepayload(ownershiptoken:).md)
  Builds an accessory setup payload with the given ownership token.
- [func makePayload(url: URL, ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md)
  Builds an accessory setup payload with the given setup payload URL and ownership token.
### Initializers
- [init()](hmaddaccessoryrequest/init.md)

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

- [func homeManager(HMHomeManager, didReceiveAddAccessoryRequest: HMAddAccessoryRequest)](hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:).md)
  Tells the delegate to add an accessory to a home by using a setup payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest)*