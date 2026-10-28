# download(_:canAuthenticateAgainstProtectionSpace:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ connection: NSURLDownload, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

```objc
- (BOOL) download:(NSURLDownload *) connection canAuthenticateAgainstProtectionSpace:(NSURLProtectionSpace *) protectionSpace;
```

## Discussion

This method is called before [`download(_:didReceive:)`](./download%28_,didreceive%29-1pc0v.md), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [`true`](../../Swift/true.md), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [`download(_:didReceive:)`](./download%28_,didreceive%29-1pc0v.md). Not implementing this method is the same as returning [`false`](../../Swift/false.md), in which case default authentication handling is used.

## Parameters

- `connection`: The download sending the message.
- `protectionSpace`: The protection space that generates an authentication challenge.

## See Also

### Download Authentication
- [func download(NSURLDownload, didCancel: URLAuthenticationChallenge)](./download%28_,didcancel%29.md)
  Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [func download(NSURLDownload, didReceive: URLAuthenticationChallenge)](./download%28_,didreceive%29-1pc0v.md)
  Sent when the URL download must authenticate a challenge in order to download the request.
- [func downloadShouldUseCredentialStorage(NSURLDownload) -> Bool](./downloadshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should consult the credential storage to authenticate the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:canauthenticateagainstprotectionspace:))*