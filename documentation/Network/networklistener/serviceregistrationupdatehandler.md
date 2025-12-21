# NetworkListener.ServiceRegistrationUpdateHandler

**Framework**: Network  
**Kind**: typealias

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
typealias ServiceRegistrationUpdateHandler = @isolated(any) (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.ServiceRegistrationChange) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/serviceregistrationupdatehandler)*