# isValidPartyCode(_:)

**Framework**: GameKit  
**Kind**: method

Checks whether a party code is in valid format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func isValidPartyCode(_ partyCode: String) -> Bool
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

Party code should be two parts of strings with the same length (2-6) connected with a dash, and the code can be either pure digits (0-9), or both parts are uppercased characters from [`validPartyCodeAlphabet`](gkgameactivity/validpartycodealphabet.md).

## See Also

- [var partyCode: String?](gkgameactivity/partycode.md)
  If the game supports party code, this is the party code that can be shared among players to join the party.
- [var partyURL: URL?](gkgameactivity/partyurl.md)
  If the game supports party code, this is the URL that can be shared among players to join the party.
- [class var validPartyCodeAlphabet: [String]](gkgameactivity/validpartycodealphabet.md)
  Allowed characters for the party code to be used to share this activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/isvalidpartycode(_:))*