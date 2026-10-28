# GKError.Code.lockdownMode

**Framework**: GameKit  
**Kind**: case  
**Role**: Case

The system can’t complete the requested operation because the player enabled Lockdown Mode on the device.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
case lockdownMode
```

```c
GKErrorLockdownMode
```

## Discussion

For more information about Lockdown Mode, see [About Lockdown Mode](https://support.apple.com/en-us/HT212650).

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
- [GKError.Code.notAuthorized](./notauthorized.md)
  The system can’t complete the requested operation because the system hasn’t authorized the player.
- [GKError.Code.iCloudUnavailable](./icloudunavailable.md)
  The system can’t complete the requested operation because it can’t access the player’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/lockdownmode)*