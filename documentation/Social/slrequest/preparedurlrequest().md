# preparedURLRequest()

**Framework**: Social  
**Kind**: method  
**Role**: Instance Method

Returns an authorized URL request that can be sent using an [`NSURLConnection`](../../Foundation/nsurlconnection.md) object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func preparedURLRequest() -> URLRequest!
```

```objc
- (NSURLRequest *) preparedURLRequest;
```

#### Return Value

An OAuth-compatible `NSURLRequest` object that allows an app to act on behalf of the user, while keeping the user’s password private. The `NSURLRequest` is signed as OAuth1 by default, or OAuth2 by adding the appropriate token based on the user’s account.

#### Discussion

Use this method to modify your request before sending. By setting the account correctly, this method will automatically add any necessary tokens.

## See Also

### Getting the Request Details
- [var requestMethod: SLRequestMethod](./requestmethod.md)
  The method to use for this request.
- [enum SLRequestMethod](../slrequestmethod.md)
  Indicates the request method used in the request.
- [var url: URL!](./url.md)
  The destination URL for this request.
- [var parameters: [AnyHashable : Any]!](./parameters.md)
  The parameters for this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slrequest/preparedurlrequest())*