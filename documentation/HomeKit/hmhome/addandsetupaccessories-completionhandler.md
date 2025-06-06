# addAndSetupAccessories(completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Finds and adds nearby accessories to the home.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Declaration

```swift
func addAndSetUpAccessories() async throws
```

## Mentions

- [Testing your app with the HomeKit Accessory Simulator](testing-your-app-with-the-homekit-accessory-simulator.md)

#### Discussion

This method launches an interactive process that first asks the user to provide a HomeKit code for the accessories—for example, by scanning an 8-digit code, by scanning the QR code, wirelessly by holding an iPhone next to the device, or by manually entering the HomeKit code. The process then asks the user to configure the accessory’s services, naming them and placing them in rooms.

## Parameters

- `completion`: The block executed after the request is processed.

## See Also

- [var accessories: [HMAccessory]](hmhome/accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](hmhome/addandsetupaccessories(with:completionhandler:).md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addandsetupaccessories(completionhandler:))*