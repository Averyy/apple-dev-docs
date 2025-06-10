# originalRequest

**Framework**: Foundation  
**Kind**: property

A deep copy of the original connection request.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var originalRequest: URLRequest { get }
```

#### Discussion

As the connection performs the load, the request may change as a result of protocol canonicalization or due to following redirects. [`currentRequest`](nsurlconnection/currentrequest.md) can be used to retrieve this value.

## See Also

- [var currentRequest: URLRequest](nsurlconnection/currentrequest.md)
  The current connection request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnection/originalrequest)*