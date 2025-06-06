# domain

**Framework**: Foundation  
**Kind**: property

The domain of the cookie.

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
var domain: String { get }
```

#### Discussion

If the domain does not start with a dot, then the cookie is only sent to the exact host specified by the domain. If the domain does start with a dot, then the cookie is sent to other hosts in that domain as well, subject to certain restrictions. See [`RFC 6265`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6265.html) for more detail.

## See Also

- [var path: String](httpcookie/path.md)
  The cookie’s path.
- [var portList: [NSNumber]?](httpcookie/portlist.md)
  The cookie’s port list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/domain)*