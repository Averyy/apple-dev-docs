# networkServiceType

**Framework**: Foundation  
**Kind**: property

The network service type of the request.

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
var networkServiceType: NSURLRequest.NetworkServiceType { get }
```

#### Discussion

The network service type provides a hint to the operating system about what the underlying traffic is used for. This hint enhances the system’s ability to prioritize traffic, determine how quickly it needs to wake up the cellular or Wi-Fi radio, and so on. By providing accurate information, you improve the ability of the system to optimally balance battery life, performance, and other considerations.

## See Also

- [var networkServiceType: NSURLRequest.NetworkServiceType](nsmutableurlrequest/networkservicetype.md)
  The network service type of the connection.
- [NSURLRequest.NetworkServiceType](nsurlrequest/networkservicetype-swift.enum.md)
  Constants that specify how a request uses network resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlrequest/networkservicetype-swift.property)*