# httpShouldHandleCookies

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL HTTPShouldHandleCookies;
```

#### Discussion

[`true`](../../Swift/true.md) if the request should use the default cookie handling for the request, [`false`](../../Swift/false.md) otherwise. The default is [`true`](../../Swift/true.md).

If your app sets the `Cookie` header on an [`NSMutableURLRequest`](../nsmutableurlrequest.md) object, then this method has no effect, and the cookie data you set in the header overrides all cookies from the cookie store.

##### Special considerations

In OS X v10.2 with Safari 1.0 the value set by this method is not respected by the framework.

## See Also

### Related Documentation
- [var httpShouldHandleCookies: Bool](../nsurlrequest/httpshouldhandlecookies.md)
  A Boolean value that indicates whether the default cookie handling will be used for this request.
### Controlling request behavior
- [var timeoutInterval: TimeInterval](./timeoutinterval.md)
  The request’s timeout interval, in seconds.
- [var httpShouldUsePipelining: Bool](./httpshouldusepipelining.md)
  A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether a connection can use the device’s cellular network (if present).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldhandlecookies)*