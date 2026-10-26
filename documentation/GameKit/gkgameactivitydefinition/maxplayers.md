# maxPlayers

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of participants that can join the activity. Returns nil when no maximum is set (unlimited players) or when player range is undefined. When not nil, the value is always greater than or equal to `minPlayers`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * maxPlayers;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition/maxplayers)*