# joinAccessoryHotspotWithoutSecurity(_:completionHandler:)

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
func joinAccessoryHotspotWithoutSecurity(_ accessory: ASAccessory, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func joinAccessoryHotspotWithoutSecurity(_ accessory: ASAccessory) async throws
```

```objc
- (void) joinAccessoryHotspotWithoutSecurity:(ASAccessory *) accessory completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager/joinaccessoryhotspotwithoutsecurity(_:completionhandler:))*