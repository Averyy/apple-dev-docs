# download(_:didReceive:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent when the URL download must authenticate a challenge in order to download the request.

**Availability**:
- macOS 10.2+

## Declaration

```swift
optional func download(_ download: NSURLDownload, didReceive challenge: URLAuthenticationChallenge)
```

```objc
- (void) download:(NSURLDownload *) download didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

#### Discussion

This method gives the delegate the opportunity to determine the course of action taken for the challenge: provide credentials, continue without providing credentials or cancel the authentication challenge and the download.

The delegate can determine the number of previous authentication challenges by sending the message [`previousFailureCount`](../urlauthenticationchallenge/previousfailurecount.md) to `challenge`.

If the previous failure count is 0 and the value returned by [`proposedCredential`](../urlauthenticationchallenge/proposedcredential.md) is `nil`, the delegate can create a new NSURLCredential object, providing information specific to the type of credential, and send a [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md) message to `[challenge sender]`, passing the credential and `challenge` as parameters. If [`proposedCredential`](../urlauthenticationchallenge/proposedcredential.md) is not `nil`, the value is a credential from the URL or the shared credential storage that can be provided to the user as feedback.

The delegate may decide to abandon further attempts at authentication at any time by sending `[challenge sender]` a [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) or a [`cancel(_:)`](../urlauthenticationchallengesender/cancel%28_%29.md) message. The specific action is implementation dependent.

If the delegate implements this method, the download will suspend until `[challenge sender]` is sent one of the following messages: [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md), [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) or [`cancel(_:)`](../urlauthenticationchallengesender/cancel%28_%29.md).

If the delegate does not implement this method the default implementation is used. If a valid credential for the request is provided as part of the URL, or is available from the NSURLCredentialStorage the `[challenge sender]` is sent a [`use(_:for:)`](../urlauthenticationchallengesender/use%28_,for%29.md) with the credential. If the challenge has no credential or the credentials fail to authorize access, then [`continueWithoutCredential(for:)`](../urlauthenticationchallengesender/continuewithoutcredential%28for%29.md) is sent to `[challenge sender]` instead.

## Parameters

- `download`: The URL download object sending the message.
- `challenge`: The URL authentication challenge that must be authenticated in order to download the request.

## See Also

### Download Authentication
- [func download(NSURLDownload, canAuthenticateAgainstProtectionSpace: URLProtectionSpace) -> Bool](./download%28_,canauthenticateagainstprotectionspace%29.md)
  Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [func download(NSURLDownload, didCancel: URLAuthenticationChallenge)](./download%28_,didcancel%29.md)
  Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [func downloadShouldUseCredentialStorage(NSURLDownload) -> Bool](./downloadshouldusecredentialstorage%28_%29.md)
  Sent to determine whether the URL loader should consult the credential storage to authenticate the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didreceive:)-1pc0v)*