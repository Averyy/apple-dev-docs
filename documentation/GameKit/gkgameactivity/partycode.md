# partyCode

**Framework**: GameKit  
**Kind**: property

If the game supports party code, this is the party code that can be shared among players to join the party.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var partyCode: String? { get }
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

If the game doesn’t support party code, this value will be `nil`. Use [`start(definition:partyCode:)`](gkgameactivity/start(definition:partycode:).md) to create a game activity with a custom party code.

## See Also

- [var partyURL: URL?](gkgameactivity/partyurl.md)
  If the game supports party code, this is the URL that can be shared among players to join the party.
- [class var validPartyCodeAlphabet: [String]](gkgameactivity/validpartycodealphabet.md)
  Allowed characters for the party code to be used to share this activity.
- [class func isValidPartyCode(String) -> Bool](gkgameactivity/isvalidpartycode(_:).md)
  Checks whether a party code is in valid format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/partycode)*