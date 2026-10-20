# GKError.Code.communicationsFailure

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The system can’t complete the requested operation due to an error communicating with the server.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case communicationsFailure
```

```c
GKErrorCommunicationsFailure
```

## See Also

### Communication Errors
- [GKError.Code.unknown](./unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [GKError.Code.cancelled](./cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [GKError.Code.invalidPlayer](./invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [GKError.Code.invalidParameter](./invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [GKError.Code.gameSessionRequestInvalid](./gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [GKError.Code.apiNotAvailable](./apinotavailable.md)
  The system can’t complete the requested operation because the API isn’t available.
- [GKError.Code.connectionTimeout](./connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [GKError.Code.apiObsolete](./apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/communicationsfailure)*