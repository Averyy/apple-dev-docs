# createAccessToken()

**Framework**: BrowserEngineKit  
**Kind**: method

Generates an opaque token that the system uses to keep your networking extension active in the background.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(createAccessToken) static func createAccessToken() -> Data?
```

#### Discussion

Use this method to generate a token that you pass to [`init(sourceURL:destinationURL:observedProgress:liveActivityAccessToken:)`](bedownloadmonitor-9bwls/init(sourceurl:destinationurl:observedprogress:liveactivityaccesstoken:).md).

## See Also

- [init(sourceURL: URL, destinationURL: URL, observedProgress: Progress, liveActivityAccessToken: Data)](bedownloadmonitor-9bwls/init(sourceurl:destinationurl:observedprogress:liveactivityaccesstoken:).md)
  Initializes a download monitor to report progress for the specified download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/createaccesstoken())*