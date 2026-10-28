# download(_:didCancel:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didCancel challenge: URLAuthenticationChallenge)
```

```objc
- (void) download:(NSURLDownload *) download didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Discussion

If the delegate receives this message the download will fail and the delegate will receive a [`download(_:didFailWithError:)`](./download%28_,didfailwitherror%29.md) message.

## Parameters

- `download`: The URL download object sending the message.
- `challenge`: The authentication challenge that caused the download object to cancel the download.

## See Also

### Download Authentication
- [func download(NSURLDownload, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./download%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func download(NSURLDownload, didReceive: URLAuthenticationChallenge)](./download%28_,didreceive%29-1pc0v.md)
  Sent when the URL download must authenticate a challenge in order to download the request.
- [func downloadShouldUseCredentialStorage(NSURLDownload) -> Bool](./downloadshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should consult the credential storage to authenticate the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didcancel:))*