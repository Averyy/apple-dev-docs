# allHeaderFields

**Framework**: Foundation  
**Kind**: property

All HTTP header fields of the response.

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
var allHeaderFields: [AnyHashable : Any] { get }
```

#### Discussion

The value of this property is a dictionary that contains all the HTTP header fields received as part of the server’s response. By examining this dictionary, clients can see the “raw” header information returned by the HTTP server.

The keys in this dictionary are the header field names, as received from the server. See [`RFC 2616`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc2616.txt) for a list of commonly used HTTP header fields.

HTTP headers are case insensitive. To simplify your code, URL Loading System canonicalizes certain header field names into their standard form. For example, if the server sends a `content-length` header, it’s automatically adjusted to be `Content-Length`.

When using Swift, this property is a standard dictionary, so its keys are case-sensitive. To perform a case-insensitive header lookup, use the [`value(forHTTPHeaderField:)`](httpurlresponse/value(forhttpheaderfield:).md) method instead.

In Objective-C, the returned dictionary of headers is case-preserving during the set operation (unless the key already exists with a different case), and case-insensitive when looking up keys.

For example, if you set the header `X-foo`, and then later set the header `X-Foo`, the dictionary’s key is be `X-foo`, but the value comes from the `X-Foo` header.

##### Special Considerations

Prior to OS X v10.7 and iOS 5, canonicalization occurred for all header fields. The case-preserving dictionary was first introduced in OS X v10.7.2 and iOS 5.

## See Also

- [func value(forHTTPHeaderField: String) -> String?](httpurlresponse/value(forhttpheaderfield:).md)
  Returns the value that corresponds to the given header field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpurlresponse/allheaderfields)*