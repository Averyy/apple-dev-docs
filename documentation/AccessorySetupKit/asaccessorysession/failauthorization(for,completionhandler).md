# failAuthorization(for:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method  
**Role**: Instance Method

End authorization of a partially-configured accessory as a failure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func failAuthorization(for accessory: ASAccessory, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func failAuthorization(for accessory: ASAccessory) async throws
```

```objc
- (void) failAuthorization:(ASAccessory *) accessory completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Managing authorization
- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](./finishauthorization%28for,settings,completionhandler%29.md)
  Finish authorization of a partially-setup accessory.
- [class ASAccessorySettings](../asaccessorysettings.md)
  Properties of an accessory.
- [func updateAuthorization(for: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: ((any Error)?) -> Void)](./updateauthorization%28for,descriptor,completionhandler%29.md)
  Displays a view to upgrade an accessory with additional technology permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/failauthorization(for:completionhandler:))*