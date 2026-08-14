# httpShouldHandleCookies

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the request should use the default cookie handling for the request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var httpShouldHandleCookies: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the request should use the default cookie handling for the request, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. The default is [`true`](https://developer.apple.com/documentation/swift/true).

If your app sets the `Cookie` header on an [`NSMutableURLRequest`](nsmutableurlrequest.md) object, then this method has no effect, and the cookie data you set in the header overrides all cookies from the cookie store.

##### Special Considerations

In OS X v10.2 with Safari 1.0 the value set by this method is not respected by the framework.

## See Also

- [var httpShouldHandleCookies: Bool](nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
- [var timeoutInterval: TimeInterval](nsmutableurlrequest/timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldUsePipelining: Bool](nsmutableurlrequest/httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](nsmutableurlrequest/allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldhandlecookies)*