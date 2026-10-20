# GKError.Code.notAuthorized

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The system can’t complete the requested operation because the system hasn’t authorized the player.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case notAuthorized
```

```c
GKErrorNotAuthorized
```

## See Also

### Player-Related Errors
- [GKError.Code.userDenied](./userdenied.md)
  The system can’t complete the requested operation because the user denied it.
- [GKError.Code.invalidCredentials](./invalidcredentials.md)
  The system can’t complete the requested operation because the user name or password are incorrect.
- [GKError.Code.notAuthenticated](./notauthenticated.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.authenticationInProgress](./authenticationinprogress.md)
  The system can’t complete the requested operation because the local player is already authenticating.
- [GKError.Code.parentalControlsBlocked](./parentalcontrolsblocked.md)
  The system can’t complete the requested operation because the user disabled this feature in Restrictions.
- [GKError.Code.playerStatusExceedsMaximumLength](./playerstatusexceedsmaximumlength.md)
  The player’s status exceeds the maximum length.
- [GKError.Code.playerStatusInvalid](./playerstatusinvalid.md)
  The player’s status is invalid.
- [GKError.Code.underage](./underage.md)
  The system can’t complete the requested operation because this feature isn’t available to underage players.
- [GKError.Code.playerPhotoFailure](./playerphotofailure.md)
  The system can’t complete the requested operation to retrieve a player’s photo.
- [GKError.Code.ubiquityContainerUnavailable](./ubiquitycontainerunavailable.md)
  The system can’t complete the requested operation because the user hasn’t signed in to iCloud or hasn’t enabled iCloud Drive.
- [GKError.Code.iCloudUnavailable](./icloudunavailable.md)
  The system can’t complete the requested operation because it can’t access the player’s iCloud account.
- [GKError.Code.lockdownMode](./lockdownmode.md)
  The system can’t complete the requested operation because the player enabled Lockdown Mode on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/notauthorized)*