# joinAccessoryHotspot(_:passphrase:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
func joinAccessoryHotspot(_ accessory: ASAccessory, passphrase: String, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func joinAccessoryHotspot(_ accessory: ASAccessory, passphrase: String) async throws
```

```objc
- (void) joinAccessoryHotspot:(ASAccessory *) accessory passphrase:(NSString *) passphrase completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/joinaccessoryhotspot(_:passphrase:completionhandler:))*