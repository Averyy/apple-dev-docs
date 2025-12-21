# download(_:didReceive:completionHandler:)

**Framework**: Background Assets  
**Kind**: method

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
optional func download(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Discussion

The completion handler takes the following parameters:

- An [`URLSession.AuthChallengeDisposition`](https://developer.apple.com/documentation/Foundation/URLSession/AuthChallengeDisposition) that indicates whether the system processes, cancels, or rejects the challenge.
- If the specified dispostion is [`URLSession.AuthChallengeDisposition.useCredential`](https://developer.apple.com/documentation/Foundation/URLSession/AuthChallengeDisposition/useCredential), the [`URLCredential`](https://developer.apple.com/documentation/Foundation/URLCredential) to use for authentication; otherwise, specify `nil`.

If you implement this method, make sure to call the completion handler promptly and with the necessary information. Otherwise, the server may deny the request and the associated asset download fails.

For more information about authentication challenges, see [`Handling an authentication challenge`](https://developer.apple.com/documentation/Foundation/handling-an-authentication-challenge).

## Parameters

- `download`: The associated asset download.
- `challenge`: An object that provides the information you need to decide how to respond to the server’s request for authentication.
- `completionHandler`: The completion handler you call to tell the system how to respond to the challenge.

## See Also

- [func downloadDidBegin(BADownload)](badownloadmanagerdelegate/downloaddidbegin(_:).md)
  Informs the delegate about a started asset download.
- [func download(BADownload, didWriteBytes: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](badownloadmanagerdelegate/download(_:didwritebytes:totalbyteswritten:totalbytesexpectedtowrite:).md)
  Informs the delegate about the progress of the specified asset download.
- [func downloadDidPause(BADownload)](badownloadmanagerdelegate/downloaddidpause(_:).md)
  Informs the delegate about a paused asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/download(_:didreceive:completionhandler:))*