# addAndSetupAccessories(with:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Finds and adds nearby accessories to the home using a HomeKit code provided by your app.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
func addAndSetUpAccessories(payload: HMAccessorySetupPayload) async throws -> [HMAccessory]
```

#### Discussion

Use this method to add accessories that have already been deployed (for example, accessories that have HomeKit support added as a firmware update), or accessories for which scanning a QR code would be difficult. Your app provides the accessory’s HomeKit code using a setup payload. For details on the payload’s content, please join the [`MFi Program`](https://developer.apple.comhttps://developer.apple.com/programs/mfi/).

During this process, the user assigns the accessory to a room and configures its services.

## Topics

### Defining the Setup Payload
- [class HMAccessorySetupPayload](hmaccessorysetuppayload.md)
  A payload for authenticating a HomeKit accessory.

## See Also

- [var accessories: [HMAccessory]](hmhome/accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](hmhome/addandsetupaccessories(completionhandler:).md)
  Finds and adds nearby accessories to the home.
- [func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/addaccessory(_:completionhandler:).md)
  Adds a new accessory to the home.
- [func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/assignaccessory(_:to:completionhandler:).md)
  Assigns an accessory to a different room.
- [func removeAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/removeaccessory(_:completionhandler:).md)
  Removes an accessory from the home.
- [var supportsAddingNetworkRouter: Bool](hmhome/supportsaddingnetworkrouter.md)
  A Boolean that indicates whether a home supports all of the requirements for adding a network router.
- [func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/unblockaccessory(_:completionhandler:).md)
  Unblocks a blocked accessory.
- [class HMAccessory](hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addandsetupaccessories(with:completionhandler:))*