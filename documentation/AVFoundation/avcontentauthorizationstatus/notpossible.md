# AVContentAuthorizationStatus.notPossible

**Framework**: AVFoundation  
**Kind**: case

The last call to request content authorization couldn’t be completed in a non-recoverable way.

**Availability**:
- macOS ?+

## Declaration

```swift
case notPossible
```

#### Discussion

This status is returned when the call can’t be completed, for example, a newer version of iTunes is required.

## See Also

- [AVContentAuthorizationStatus.unknown](avcontentauthorizationstatus/unknown.md)
  The content authorization content request hasn’t completed.
- [AVContentAuthorizationStatus.completed](avcontentauthorizationstatus/completed.md)
  The last completed call to request content authorization completed.
- [AVContentAuthorizationStatus.cancelled](avcontentauthorizationstatus/cancelled.md)
  The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationStatus.timedOut](avcontentauthorizationstatus/timedout.md)
  The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationStatus.busy](avcontentauthorizationstatus/busy.md)
  The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationStatus.notAvailable](avcontentauthorizationstatus/notavailable.md)
  The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/notpossible)*