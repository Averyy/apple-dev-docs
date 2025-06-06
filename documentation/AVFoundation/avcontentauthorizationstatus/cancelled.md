# AVContentAuthorizationStatus.cancelled

**Framework**: AVFoundation  
**Kind**: case

The last call to request content authorization was cancelled by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
case cancelled
```

## See Also

- [AVContentAuthorizationStatus.unknown](avcontentauthorizationstatus/unknown.md)
  The content authorization content request hasn’t completed.
- [AVContentAuthorizationStatus.completed](avcontentauthorizationstatus/completed.md)
  The last completed call to request content authorization completed.
- [AVContentAuthorizationStatus.timedOut](avcontentauthorizationstatus/timedout.md)
  The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationStatus.busy](avcontentauthorizationstatus/busy.md)
  The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationStatus.notAvailable](avcontentauthorizationstatus/notavailable.md)
  The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.
- [AVContentAuthorizationStatus.notPossible](avcontentauthorizationstatus/notpossible.md)
  The last call to request content authorization couldn’t be completed in a non-recoverable way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/cancelled)*