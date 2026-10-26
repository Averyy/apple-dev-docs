# backgroundDownload(_:didReceive:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Handles an authentication challenge.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func backgroundDownload(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Return Value

The disposition with which to respond to the authentication challenge and the credential, if any, to use while doing so.

#### Discussion

If your app doesn’t use Apple hosting, then you can override this default implementation to provide your own handling for authentication challenges from your server.

## Parameters

- `download`: The download for which the server presented the authentication challenge.
- `challenge`: The authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:didreceive:)-7qfcp)*