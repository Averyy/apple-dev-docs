# initWithWebPageURL:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a new media playback environment identified for a webpage URL.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```objc
- (instancetype) initWithWebPageURL:(NSURL *) url;
```

## Parameters

- `url`: The URL that identifies the media playback environment.

## See Also

### Managing media life cycle
- [- initWithXPCRepresentation:error:](./initwithxpcrepresentation_error_.md)
  Creates a media session from an XPC object.
- [- activateWithError:](./activatewitherror_.md)
  Activates the media environment.
- [- suspendWithError:](./suspendwitherror_.md)
  Suspends the media environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-n91a/initwithwebpageurl:)*