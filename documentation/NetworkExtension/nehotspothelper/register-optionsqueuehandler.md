# register(options:queue:handler:)

**Framework**: Network Extension  
**Kind**: method

Register the application as a Hotspot Helper.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func register(options: [String : NSObject]? = nil, queue: dispatch_queue_t, handler: @escaping NEHotspotHelperHandler) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the registration was successful, [`false`](https://developer.apple.com/documentation/swift/false) otherwise

#### Discussion

Once this API is invoked successfully, the application becomes eligible to be launched in the background and participate in various hotspot related functions.

This method should be called once when the application starts up. Invoking it again will have no effect and result in [`false`](https://developer.apple.com/documentation/swift/false) being returned.

> ⚠️ **Warning**:  The application’s `Info.plist` must include a `UIBackgroundModes` array containing `network-authentication`.

 The application’s `Info.plist` must include a `UIBackgroundModes` array containing `network-authentication`.

> ⚠️ **Warning**:  The application must set `com.apple.developer.networking.HotspotHelper` as one of its entitlements. The value of the entitlement is a boolean set to `true`.

 The application must set `com.apple.developer.networking.HotspotHelper` as one of its entitlements. The value of the entitlement is a boolean set to `true`.

## Parameters

- `options`: If not nil, a   containing   keys (currently just  ).
- `queue`: The   to invoke the handle block on.
- `handler`: The   block to execute to process helper commands.

## See Also

- [let kNEHotspotHelperOptionDisplayName: String](knehotspothelperoptiondisplayname.md)
  The string displayed in Wi-Fi Settings for a network handled by the application.
- [typealias NEHotspotHelperHandler](nehotspothelperhandler.md)
  The type definition for the Hotspot Helper’s command handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelper/register(options:queue:handler:))*