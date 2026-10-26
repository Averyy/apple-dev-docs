# initWithXPCRepresentation:error:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a media session from an XPC object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```objc
- (instancetype) initWithXPCRepresentation:(xpc_object_t) xpcRepresentation error:(NSError **) error;
```

## Parameters

- `xpcRepresentation`: A representation of a media environment the app receives through XPC.
- `error`: A pointer to an error object that describes why the method failed, or `nil` if no error occurred. Pass `nil` to ignore the error.

## See Also

### Managing media life cycle
- [- initWithWebPageURL:](./initwithwebpageurl_.md)
  Creates a new media playback environment identified for a webpage URL.
- [- activateWithError:](./activatewitherror_.md)
  Activates the media environment.
- [- suspendWithError:](./suspendwitherror_.md)
  Suspends the media environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-n91a/initwithxpcrepresentation:error:)*