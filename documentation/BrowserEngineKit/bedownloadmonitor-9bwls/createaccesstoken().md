# createAccessToken()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

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

Use this method to generate a token that you pass to [`init(sourceURL:destinationURL:observedProgress:liveActivityAccessToken:)`](./init%28sourceurl,destinationurl,observedprogress,liveactivityaccesstoken%29.md).

## See Also

### Creating a download monitor
- [init(sourceURL: URL, destinationURL: URL, observedProgress: Progress, liveActivityAccessToken: Data)](./init%28sourceurl,destinationurl,observedprogress,liveactivityaccesstoken%29.md)
  Initializes a download monitor to report progress for the specified download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/createaccesstoken())*