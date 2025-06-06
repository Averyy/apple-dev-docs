# networkServiceType

**Framework**: Foundation  
**Kind**: property

The network service type of the connection.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var networkServiceType: NSURLRequest.NetworkServiceType { get set }
```

#### Discussion

The network service type provides a hint to the operating system about what the underlying traffic is used for. This hint enhances the system’s ability to prioritize traffic, determine how quickly it needs to wake up the cellular or Wi-Fi radio, and so on. By providing accurate information, you improve the ability of the system to optimally balance battery life, performance, and other considerations.

For example, specify the [`NSURLRequest.NetworkServiceType.background`](nsurlrequest/networkservicetype-swift.enum/background.md) type if your app is performing a download that was not requested by the user, like prefetching content so that it’s available when the user chooses to view it. By contrast, continually connected voice and video apps should use the [`NSURLRequest.NetworkServiceType.voice`](nsurlrequest/networkservicetype-swift.enum/voice.md),  [`NSURLRequest.NetworkServiceType.voip`](nsurlrequest/networkservicetype-swift.enum/voip.md), or [`NSURLRequest.NetworkServiceType.video`](nsurlrequest/networkservicetype-swift.enum/video.md) service types, as appropriate.

## See Also

- [NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/networkservicetype)*