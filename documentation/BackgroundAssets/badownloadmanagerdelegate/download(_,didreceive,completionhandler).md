# download(_:didReceive:completionHandler:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to resolve the specified URL authentication challenge.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func download(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge, completionHandler: @escaping @Sendable (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)
```

```swift
optional func download(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

```objc
- (void) download:(BADownload *) download didReceiveChallenge:(NSURLAuthenticationChallenge *) challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential *credential)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- An [`URLSession.AuthChallengeDisposition`](../../Foundation/urlsession/authchallengedisposition.md) that indicates whether the system processes, cancels, or rejects the challenge.
- If the specified dispostion is [`URLSession.AuthChallengeDisposition.useCredential`](../../Foundation/urlsession/authchallengedisposition/usecredential.md), the [`URLCredential`](../../Foundation/urlcredential.md) to use for authentication; otherwise, specify `nil`.

If you implement this method, make sure to call the completion handler promptly and with the necessary information. Otherwise, the server may deny the request and the associated asset download fails.

For more information about authentication challenges, see [Handling an authentication challenge](../../Foundation/handling-an-authentication-challenge.md).

## Parameters

- `download`: The associated asset download.
- `challenge`: An object that provides the information you need to decide how to respond to the server’s request for authentication.
- `completionHandler`: The completion handler you call to tell the system how to respond to the challenge.

## See Also

### Reacting to download events
- [func downloadDidBegin(BADownload)](./downloaddidbegin%28_%29.md)
  Informs the delegate about a started asset download.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](./download%28_,didwritebytes,totalbyteswritten,totalbytesexpectedtowrite%29.md)
  Informs the delegate about the progress of the specified asset download.
- [func downloadDidPause(BADownload)](./downloaddidpause%28_%29.md)
  Informs the delegate about a paused asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/download(_:didreceive:completionhandler:))*