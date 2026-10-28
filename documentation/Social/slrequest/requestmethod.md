# requestMethod

**Framework**: Social  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) SLRequestMethod requestMethod;
```

## Discussion

Use this property to look up the method of the HTTP request that was set in [`init(forServiceType:requestMethod:url:parameters:)`](./init%28forservicetype,requestmethod,url,parameters%29-2cnf1.md). Possible values are described in [`SLRequestMethod`](../slrequestmethod.md).

## See Also

### Getting the Request Details
- [func preparedURLRequest() -> URLRequest!](./preparedurlrequest%28%29.md)
  Returns an authorized URL request that can be sent using an [`NSURLConnection`](../../Foundation/nsurlconnection.md) object.
- [enum SLRequestMethod](../slrequestmethod.md)
  Indicates the request method used in the request.
- [var url: URL!](./url.md)
  The destination URL for this request.
- [var parameters: [AnyHashable : Any]!](./parameters.md)
  The parameters for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/requestmethod)*