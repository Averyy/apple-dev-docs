# register(options:queue:handler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Register the application as a Hotspot Helper.

**Availability**:
- iOS 9.0+ - Deprecated in 26.0
- iPadOS 9.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use NEHotspotManager API

## Declaration

```swift
class func register(options: [String : NSObject]? = nil, queue: dispatch_queue_t, handler: @escaping NEHotspotHelperHandler) -> Bool
```

```objc
+ (BOOL) registerWithOptions:(NSDictionary<NSString *,NSObject *> *) options queue:(dispatch_queue_t) queue handler:(NEHotspotHelperHandler) handler;
```

## Return Value

[`true`](../../Swift/true.md) if the registration was successful, [`false`](../../Swift/false.md) otherwise

## Discussion

Once this API is invoked successfully, the application becomes eligible to be launched in the background and participate in various hotspot related functions.

This method should be called once when the application starts up. Invoking it again will have no effect and result in [`false`](../../Swift/false.md) being returned.

> ⚠️ **Warning**:  The application’s `Info.plist` must include a `UIBackgroundModes` array containing `network-authentication`.

> ⚠️ **Warning**:  The application must set `com.apple.developer.networking.HotspotHelper` as one of its entitlements. The value of the entitlement is a boolean set to `true`.

## Parameters

- `options`: If not nil, a [`NSDictionary`](../../Foundation/nsdictionary.md) containing `kNEHotspotHelperOption*` keys (currently just `kNEHotspotHelperOptionDisplayName`).
- `queue`: The [`dispatch_queue_t`](../../Dispatch/dispatch_queue_t.md) to invoke the handle block on.
- `handler`: The `NEHotspotHelperHandler` block to execute to process helper commands.

## See Also

### Registering a hotspot helper
- [let kNEHotspotHelperOptionDisplayName: String](../knehotspothelperoptiondisplayname.md)
  The string displayed in Wi-Fi Settings for a network handled by the application.
- [typealias NEHotspotHelperHandler](../nehotspothelperhandler.md)
  The type definition for the Hotspot Helper’s command handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelper/register(options:queue:handler:))*