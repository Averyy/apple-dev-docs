# deviceName

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The name of the device that the player uses to save the game.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var deviceName: String? { get }
```

```objc
@property (atomic, readonly, nullable) NSString * deviceName;
```

## Discussion

In iOS, the user sets the device name by choosing Settings > General > About > Name. To access this device name, your app needs to meet certain criteria and set the [`com.apple.developer.device-information.user-assigned-device-name`](../../BundleResources/entitlements/com.apple.developer.device-information.user-assigned-device-name.md) entitlement. Otherwise, the default value for this property is the generic device name.

> **Note**:  In iOS 15 and earlier, the default value for this property is the user-assigned device name in Settings.

## See Also

### Retrieving Information About a Saved Game File
- [var name: String?](./name.md)
  The name of the saved game.
- [var modificationDate: Date?](./modificationdate.md)
  The date when you saved the game data or modified it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksavedgame/devicename)*