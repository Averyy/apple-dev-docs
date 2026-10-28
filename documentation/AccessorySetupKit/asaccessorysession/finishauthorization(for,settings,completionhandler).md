# finishAuthorization(for:settings:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method  
**Role**: Instance Method

Finish authorization of a partially-setup accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func finishAuthorization(for accessory: ASAccessory, settings: ASAccessorySettings, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func finishAuthorization(for accessory: ASAccessory, settings: ASAccessorySettings) async throws
```

```objc
- (void) finishAuthorization:(ASAccessory *) accessory settings:(ASAccessorySettings *) settings completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

Use this method in scenarios where an accessory has multiple wireless interfaces. For example, when an accessory has both Bluetooth and Wi-Fi, and your descriptor may only provides an SSID prefix. In this case, the Bluetooth interface onboards first and your app needs to then finish authorization with the full SSID.

## See Also

### Managing authorization
- [class ASAccessorySettings](../asaccessorysettings.md)
  Properties of an accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](./failauthorization%28for,completionhandler%29.md)
  End authorization of a partially-configured accessory as a failure.
- [func updateAuthorization(for: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: ((any Error)?) -> Void)](./updateauthorization%28for,descriptor,completionhandler%29.md)
  Displays a view to upgrade an accessory with additional technology permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/finishauthorization(for:settings:completionhandler:))*