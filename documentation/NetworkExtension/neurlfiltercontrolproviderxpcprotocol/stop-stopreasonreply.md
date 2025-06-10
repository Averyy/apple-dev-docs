# stop(stopReason:reply:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@objc
func stop(stopReason: NEProviderStopReason, reply: @escaping (Bool, (any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolproviderxpcprotocol/stop(stopreason:reply:))*