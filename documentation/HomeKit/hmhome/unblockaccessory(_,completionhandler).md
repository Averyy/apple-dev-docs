# unblockAccessory(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Unblocks a blocked accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func unblockAccessory(_ accessory: HMAccessory) async throws
```

```objc
- (void) unblockAccessory:(HMAccessory *) accessory completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

A misbehaving accessory automatically becomes blocked. After that, all requests to the accessory fail. Use this API to explicitly unblock the accessory.

## Parameters

- `accessory`: The accessory to unblock.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Managing accessories
- [var accessories: [HMAccessory]](./accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](./addandsetupaccessories%28completionhandler%29.md)
  Finds and adds nearby accessories to the home.
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
- [class HMAccessory](../hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/unblockaccessory(_:completionhandler:))*