# NetworkListener.ServiceRegistrationUpdateHandler

**Framework**: Network  
**Kind**: typealias

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
typealias ServiceRegistrationUpdateHandler = @isolated(any) (NetworkListener<ApplicationProtocol>, NWListener.ServiceRegistrationChange) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/serviceregistrationupdatehandler)*