# backgroundDownload(_:didReceive:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Download is about to begin but requires an authentication challenge to continue.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func backgroundDownload(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Return Value

A tuple that informs the subsystem how the challenge request shall be answered.

## Parameters

- `download`: The download object that this challenge request is for.
- `challenge`: The challenge that been received and needs to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:didreceive:)-5vjx7)*