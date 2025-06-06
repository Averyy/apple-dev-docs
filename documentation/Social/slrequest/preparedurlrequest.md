# preparedURLRequest()

**Framework**: Social  
**Kind**: method

Returns an authorized URL request that can be sent using an [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func preparedURLRequest() -> URLRequest!
```

#### Return Value

An OAuth-compatible `NSURLRequest` object that allows an app to act on behalf of the user, while keeping the user’s password private. The `NSURLRequest` is signed as OAuth1 by default, or OAuth2 by adding the appropriate token based on the user’s account.

#### Discussion

Use this method to modify your request before sending. By setting the account correctly, this method will automatically add any necessary tokens.

## See Also

- [var requestMethod: SLRequestMethod](slrequest/requestmethod.md)
  The method to use for this request.
- [enum SLRequestMethod](slrequestmethod.md)
  Indicates the request method used in the request.
- [var url: URL!](slrequest/url.md)
  The destination URL for this request.
- [var parameters: [AnyHashable : Any]!](slrequest/parameters.md)
  The parameters for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/preparedurlrequest())*