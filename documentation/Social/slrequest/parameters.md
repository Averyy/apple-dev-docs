# parameters

**Framework**: Social  
**Kind**: property

The parameters for this request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
var parameters: [AnyHashable : Any]! { get }
```

#### Discussion

Use this property to look up the query parameters of the HTTP request that was set in [`init(forServiceType:requestMethod:url:parameters:)`](slrequest/init(forservicetype:requestmethod:url:parameters:).md). Possible values are dependent on the target service and are documented by the service provider. For links to documentation for the supported services, see Table 1 in [`SLRequest`](slrequest.md).

## See Also

- [func preparedURLRequest() -> URLRequest!](slrequest/preparedurlrequest.md)
  Returns an authorized URL request that can be sent using an [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) object.
- [var requestMethod: SLRequestMethod](slrequest/requestmethod.md)
  The method to use for this request.
- [enum SLRequestMethod](slrequestmethod.md)
  Indicates the request method used in the request.
- [var url: URL!](slrequest/url.md)
  The destination URL for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/parameters)*