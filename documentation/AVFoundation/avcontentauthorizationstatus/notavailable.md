# AVContentAuthorizationStatus.notAvailable

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The last call to request content authorization couldn’t be completed because there was no known mechanism by which to attempt authorization.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case notAvailable
```

```c
AVContentAuthorizationNotAvailable
```

## See Also

### Content authorization statuses
- [AVContentAuthorizationStatus.unknown](./unknown.md)
  The content authorization content request hasn’t completed.
- [AVContentAuthorizationStatus.completed](./completed.md)
  The last completed call to request content authorization completed.
- [AVContentAuthorizationStatus.cancelled](./cancelled.md)
  The last call to request content authorization was cancelled by the user.
- [AVContentAuthorizationStatus.timedOut](./timedout.md)
  The last call to request content authorization was cancelled because the timeout interval was reached.
- [AVContentAuthorizationStatus.busy](./busy.md)
  The last call to request content authorization couldn’t be completed because another asset is currently attempting authorization.
- [AVContentAuthorizationStatus.notPossible](./notpossible.md)
  The last call to request content authorization couldn’t be completed in a non-recoverable way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentauthorizationstatus/notavailable)*