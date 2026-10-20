# GKError.Code.apiNotAvailable

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The system can’t complete the requested operation because the API isn’t available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case apiNotAvailable
```

```c
GKErrorAPINotAvailable
```

## See Also

### Communication Errors
- [GKError.Code.unknown](./unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [GKError.Code.cancelled](./cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [GKError.Code.communicationsFailure](./communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [GKError.Code.invalidPlayer](./invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [GKError.Code.invalidParameter](./invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [GKError.Code.gameSessionRequestInvalid](./gamesessionrequestinvalid.md)
  The properties of the game session request are impossible to fulfill.
- [GKError.Code.connectionTimeout](./connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [GKError.Code.apiObsolete](./apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/apinotavailable)*