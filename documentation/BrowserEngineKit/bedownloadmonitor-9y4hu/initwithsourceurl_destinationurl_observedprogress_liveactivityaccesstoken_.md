# initWithSourceURL:destinationURL:observedProgress:liveActivityAccessToken:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Initializes a download monitor to report progress for the specified download.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
- (instancetype) initWithSourceURL:(NSURL *) sourceURL destinationURL:(NSURL *) destinationURL observedProgress:(NSProgress *) observedProgress liveActivityAccessToken:(NSData *) liveActivityAccessToken;
```

#### Discussion

Generate an access token for the download by calling [`createAccessToken`](./createaccesstoken.md).

## Parameters

- `sourceURL`: The location of the resource on the web that someone wants to download.
- `destinationURL`: The location of the file to which you save the resource.
- `observedProgress`: An object that you use to report the download’s progress to the system.
- `liveActivityAccessToken`: An opaque token that the system checks to verify that your networking extension can remain active while the download is in progress.

## See Also

### Creating a download monitor
- [+ createAccessToken](./createaccesstoken.md)
  Generates an opaque token that the system uses to keep your networking extension active in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu/initwithsourceurl:destinationurl:observedprogress:liveactivityaccesstoken:)*