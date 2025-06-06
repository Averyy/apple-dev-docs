# GKError.Code.friendListDescriptionMissing

**Framework**: GameKit  
**Kind**: case

Access to the local player’s list of friends denied for lack of a reason.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 7.4+

## Declaration

```swift
case friendListDescriptionMissing
```

#### Discussion

If your game wants access to the player’s friends, provide a reason by adding the [`NSGKFriendListUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSGKFriendListUsageDescription) key to the information property list.

## See Also

- [GKError.Code.friendListRestricted](gkerror/code/friendlistrestricted.md)
  Access to the local player’s list of friends restricted.
- [GKError.Code.friendListDenied](gkerror/code/friendlistdenied.md)
  Access to the local player’s list of friends denied.
- [GKError.Code.friendRequestNotAvailable](gkerror/code/friendrequestnotavailable.md)
  The player can’t send a friend request at this time from this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/friendlistdescriptionmissing)*