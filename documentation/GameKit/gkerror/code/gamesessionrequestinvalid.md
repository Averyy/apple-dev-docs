# GKError.Code.gameSessionRequestInvalid

**Framework**: GameKit  
**Kind**: case

The properties of the game session request are impossible to fulfill.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case gameSessionRequestInvalid
```

#### Discussion

For example, the maximum number of requested players is greater than the maximum number of allowed players.

## See Also

- [GKError.Code.unknown](gkerror/code/unknown.md)
  The system can’t complete the requested operation due to an unknown error.
- [GKError.Code.cancelled](gkerror/code/cancelled.md)
  The system canceled the requested operation or the user disabled it.
- [GKError.Code.communicationsFailure](gkerror/code/communicationsfailure.md)
  The system can’t complete the requested operation due to an error communicating with the server.
- [GKError.Code.invalidPlayer](gkerror/code/invalidplayer.md)
  The system can’t complete the requested operation because the player is invalid.
- [GKError.Code.invalidParameter](gkerror/code/invalidparameter.md)
  The system can’t complete the requested operation because one or more parameters are invalid.
- [GKError.Code.apiNotAvailable](gkerror/code/apinotavailable.md)
  The system can’t complete the requested operation because the API isn’t available.
- [GKError.Code.connectionTimeout](gkerror/code/connectiontimeout.md)
  The system can’t complete the requested operation because the connection timed out.
- [GKError.Code.apiObsolete](gkerror/code/apiobsolete.md)
  The system can’t complete the requested operation because Apple deprecated the API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/gamesessionrequestinvalid)*