# requestMethod

**Framework**: Social  
**Kind**: property

The method to use for this request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var requestMethod: SLRequestMethod { get }
```

#### Discussion

Use this property to look up the method of the HTTP request that was set in [`init(forServiceType:requestMethod:url:parameters:)`](slrequest/init(forservicetype:requestmethod:url:parameters:).md). Possible values are described in [`SLRequestMethod`](slrequestmethod.md).

## See Also

- [func preparedURLRequest() -> URLRequest!](slrequest/preparedurlrequest.md)
  Returns an authorized URL request that can be sent using an [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) object.
- [enum SLRequestMethod](slrequestmethod.md)
  Indicates the request method used in the request.
- [var url: URL!](slrequest/url.md)
  The destination URL for this request.
- [var parameters: [AnyHashable : Any]!](slrequest/parameters.md)
  The parameters for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/requestmethod)*