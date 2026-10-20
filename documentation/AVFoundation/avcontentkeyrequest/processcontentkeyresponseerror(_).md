# processContentKeyResponseError(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver that the app was unable to obtain a content key response.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func processContentKeyResponseError(_ error: any Error)
```

```objc
- (void) processContentKeyResponseError:(NSError *) error;
```

## Parameters

- `error`: An [`NSError`](../../Foundation/nserror.md) that describes why the content key response failed.

## See Also

### Responding to the content key request
- [func processContentKeyResponse(AVContentKeyResponse)](./processcontentkeyresponse%28_%29.md)
  Sends the specified content key response to the receiver for processing.
- [func respondByRequestingPersistableContentKeyRequest()](./respondbyrequestingpersistablecontentkeyrequest%28%29.md)
  Tells the receiver that the app requires a persistable content key request object for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/processcontentkeyresponseerror(_:))*