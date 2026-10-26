# cancel

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Clients should call this if the current segment is to be cancelled, but the export is still expected to be resumed at a later time. For example, this could happen if the export is running in the background and the expiration handler is called due to changes in system conditions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) cancel;
```

#### Discussion

This method throws NSGenericException if finish, finishWithClientState:, finishWithError:, or cancel has already been called on this request.

## See Also

### Finishing the request
- [- finish](./finish.md)
  Clients must call this method after all writing activities for the intermediate segment file have successfully completed.
- [- finishWithError:](./finishwitherror_.md)
  Clients must call this method if a non-recoverable error occurs while generating the segment file. The completionHandler of AVAssetWritingPlanner will be called with an error whose code is AVErrorAssetWritingPlannerClientWritingError, and the error provided here will be available in the NSUnderlyingErrorKey of the userInfo dictionary. If called with nil, this is equivalent to calling finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedsegmentwritingrequest/cancel)*