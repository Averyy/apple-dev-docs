# downloadShouldUseCredentialStorage(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent to determine whether the URL loader should consult the credential storage to authenticate the download.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func downloadShouldUseCredentialStorage(_ download: NSURLDownload) -> Bool
```

```objc
- (BOOL) downloadShouldUseCredentialStorage:(NSURLDownload *) download;
```

#### Discussion

This method is called before any attempt to authenticate is made.  By returning [`false`](../../Swift/false.md), the delegate tells the download not to consult the credential storage and makes itself responsible for providing credentials for any authentication challenges.  Not implementing this method is the same as returing [`true`](../../Swift/true.md). The delegate is free to consult the credential storage itself when it receives a [`download(_:didReceive:)`](./download%28_,didreceive%29-1pc0v.md) message.

## Parameters

- `download`: The connection sending the message.

## See Also

### Download Authentication
- [func download(NSURLDownload, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./download%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func download(NSURLDownload, didCancel: URLAuthenticationChallenge)](./download%28_,didcancel%29.md)
  Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [func download(NSURLDownload, didReceive: URLAuthenticationChallenge)](./download%28_,didreceive%29-1pc0v.md)
  Sent when the URL download must authenticate a challenge in order to download the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/downloadshouldusecredentialstorage(_:))*