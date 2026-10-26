# createAccessToken

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

Generates an opaque token that the system uses to keep your networking extension active in the background.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
+ (NSData *) createAccessToken;
```

#### Discussion

Use this method to generate a token that you pass to [`initWithSourceURL:destinationURL:observedProgress:liveActivityAccessToken:`](./initwithsourceurl_destinationurl_observedprogress_liveactivityaccesstoken_.md).

## See Also

### Creating a download monitor
- [- initWithSourceURL:destinationURL:observedProgress:liveActivityAccessToken:](./initwithsourceurl_destinationurl_observedprogress_liveactivityaccesstoken_.md)
  Initializes a download monitor to report progress for the specified download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu/createaccesstoken)*