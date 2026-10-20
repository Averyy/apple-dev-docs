# anonymousGuestPlayer(withIdentifier:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Creates a guest player with the specified identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func anonymousGuestPlayer(withIdentifier guestIdentifier: String) -> Self
```

```objc
+ (instancetype) anonymousGuestPlayerWithIdentifier:(NSString *) guestIdentifier;
```

#### Return Value

A player object that represents the guest.

#### Discussion

You can treat a guest player the same as an initialized player in regard to matchmaking services.

## Parameters

- `guestIdentifier`: An identifier to use for the guest player.

## See Also

### Creating a guest player
- [var guestIdentifier: String?](./guestidentifier.md)
  A developer-created string that identifies a guest player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayer/anonymousguestplayer(withidentifier:))*