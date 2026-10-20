# partyURL

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

If the game supports party code, this is the URL that can be shared among players to join the party.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var partyURL: URL? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSURL * partyURL;
```

## See Also

### Getting and verifying the party code
- [var partyCode: String?](./partycode.md)
  If the game supports party code, this is the party code that can be shared among players to join the party.
- [class var validPartyCodeAlphabet: [String]](./validpartycodealphabet.md)
  Allowed characters for the party code to be used to share this activity.
- [class func isValidPartyCode(String) -> Bool](./isvalidpartycode%28_%29.md)
  Checks whether a party code is in valid format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/partyurl)*