# timeoutInterval

**Framework**: Foundation  
**Kind**: property

The request’s timeout interval, in seconds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var timeoutInterval: TimeInterval { get set }
```

#### Discussion

If during a connection attempt the request remains idle for longer than the timeout interval, the request is considered to have timed out. The default timeout interval is 60 seconds.

As a general rule, you should not use short timeout intervals. Instead, you should provide an easy way for the user to cancel a long-running operation. For more information, read [`Designing for Real-World Networks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/WhyNetworkingIsHard/WhyNetworkingIsHard.html#//apple_ref/doc/uid/TP40010220-CH13) in [`Networking Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010220).

##### Special Considerations

In iOS versions prior to iOS 6, the minimum (and default) timeout interval for any request containing a request body was 240 seconds.

## See Also

- [var httpShouldHandleCookies: Bool](nsmutableurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [var httpShouldUsePipelining: Bool](nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/timeoutinterval)*