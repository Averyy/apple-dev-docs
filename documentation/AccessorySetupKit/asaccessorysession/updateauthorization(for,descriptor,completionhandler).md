# updateAuthorization(for:descriptor:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method  
**Role**: Instance Method

Displays a view to upgrade an accessory with additional technology permissions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func updateAuthorization(for accessory: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateAuthorization(for accessory: ASAccessory, descriptor: ASDiscoveryDescriptor) async throws
```

```objc
- (void) updateAuthorization:(ASAccessory *) accessory descriptor:(ASDiscoveryDescriptor *) descriptor completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

Call this method to upgrade previously-added SSID-based accessories to use WiFi Aware.

## Parameters

- `accessory`: The accessory to update.
- `descriptor`: An updated descriptor that the picker uses to add new technology authorization for the provided accessory.
- `completionHandler`: A block or closure that executes after the picker is shown. The completion handler receives an [`NSError`](../../Foundation/nserror.md) instance if the upgrade operation encounters an error. In Swift, you can omit the completion handler by calling the method asynchronously and catching any error thrown by the method.

## See Also

### Managing authorization
- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](./finishauthorization%28for,settings,completionhandler%29.md)
  Finish authorization of a partially-setup accessory.
- [class ASAccessorySettings](../asaccessorysettings.md)
  Properties of an accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](./failauthorization%28for,completionhandler%29.md)
  End authorization of a partially-configured accessory as a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/updateauthorization(for:descriptor:completionhandler:))*