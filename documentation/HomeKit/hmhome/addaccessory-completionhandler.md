# addAccessory(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a new accessory to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addAccessory(_ accessory: HMAccessory) async throws
```

#### Discussion

You discover accessories to add to a home using the [`HMAccessoryBrowser`](hmaccessorybrowser.md) class. Newly added accessories are automatically added to the room returned by [`roomForEntireHome()`](hmhome/roomforentirehome().md).

> ❗ **Important**:  To provide a consistent user experience, use the [`addAndSetupAccessories(completionHandler:)`](hmhome/addandsetupaccessories(completionhandler:).md) method instead.

 To provide a consistent user experience, use the [`addAndSetupAccessories(completionHandler:)`](hmhome/addandsetupaccessories(completionhandler:).md) method instead.

## Parameters

- `accessory`: The accessory to add to the home.
- `completion`: The block executed after the request is processed.

## See Also

- [var accessories: [HMAccessory]](hmhome/accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](hmhome/addandsetupaccessories(completionhandler:).md)
  Finds and adds nearby accessories to the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](hmhome/addandsetupaccessories(with:completionhandler:).md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addaccessory(_:completionhandler:))*