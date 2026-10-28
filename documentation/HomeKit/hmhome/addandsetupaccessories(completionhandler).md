# addAndSetupAccessories(completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Finds and adds nearby accessories to the home.

**Availability**:
- iOS 10.0+ - Deprecated in 15.4
- iPadOS 10.0+ - Deprecated in 15.4
- Mac Catalyst 10.0+ - Deprecated in 15.4

> **Deprecated**: Use -[HMAccessorySetupManager performAccessorySetupUsingRequest:completionHandler:] instead

## Declaration

```swift
func addAndSetupAccessories(completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func addAndSetUpAccessories() async throws
```

```objc
- (void) addAndSetupAccessoriesWithCompletionHandler:(void (^)(NSError *error)) completion;
```

## Mentions

- [Testing your app with the HomeKit Accessory Simulator](../testing-your-app-with-the-homekit-accessory-simulator.md)

## Discussion

This method launches an interactive process that first asks the user to provide a HomeKit code for the accessories—for example, by scanning an 8-digit code, by scanning the QR code, wirelessly by holding an iPhone next to the device, or by manually entering the HomeKit code. The process then asks the user to configure the accessory’s services, naming them and placing them in rooms.

## Parameters

- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Managing accessories
- [var accessories: [HMAccessory]](./accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](./addandsetupaccessories%28with,completionhandler%29.md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
- [func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./addaccessory%28_,completionhandler%29.md)
  Adds a new accessory to the home.
- [func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)](./assignaccessory%28_,to,completionhandler%29.md)
  Assigns an accessory to a different room.
- [func removeAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./removeaccessory%28_,completionhandler%29.md)
  Removes an accessory from the home.
- [var supportsAddingNetworkRouter: Bool](./supportsaddingnetworkrouter.md)
  A Boolean that indicates whether a home supports all of the requirements for adding a network router.
- [func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](./unblockaccessory%28_,completionhandler%29.md)
  Unblocks a blocked accessory.
- [class HMAccessory](../hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addandsetupaccessories(completionhandler:))*