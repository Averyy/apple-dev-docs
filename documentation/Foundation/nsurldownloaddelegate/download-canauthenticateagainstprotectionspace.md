# download(_:canAuthenticateAgainstProtectionSpace:)

**Framework**: Foundation  
**Kind**: method

Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ connection: NSURLDownload, canAuthenticateAgainstProtectionSpace protectionSpace: URLProtectionSpace) -> Bool
```

#### Discussion

This method is called before [`download(_:didReceive:)`](nsurldownloaddelegate/download(_:didreceive:)-1pc0v.md), allowing the delegate to inspect a protection space before attempting to authenticate against it. By returning [`true`](https://developer.apple.com/documentation/Swift/true), the delegate indicates that it can handle the form of authentication, which it does in the subsequent call to [`download(_:didReceive:)`](nsurldownloaddelegate/download(_:didreceive:)-1pc0v.md). Not implementing this method is the same as returning [`false`](https://developer.apple.com/documentation/Swift/false), in which case default authentication handling is used.

## Parameters

- `connection`: The download sending the message.
- `protectionSpace`: The protection space that generates an authentication challenge.

## See Also

- [func download(NSURLDownload, didCancel: URLAuthenticationChallenge)](nsurldownloaddelegate/download(_:didcancel:).md)
  Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [func download(NSURLDownload, didReceive: URLAuthenticationChallenge)](nsurldownloaddelegate/download(_:didreceive:)-1pc0v.md)
  Sent when the URL download must authenticate a challenge in order to download the request.
- [func downloadShouldUseCredentialStorage(NSURLDownload) -> Bool](nsurldownloaddelegate/downloadshouldusecredentialstorage(_:).md)
  Sent to determine whether the URL loader should consult the credential storage to authenticate the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:canauthenticateagainstprotectionspace:))*