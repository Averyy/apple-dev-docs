# displayName

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The Game Center profile name for a player.

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
var displayName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSString * displayName;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSString * displayName;
```

#### Discussion

Players only see the display name of other players who are in their contacts list.

## See Also

### Identifying a Player
- [var playerID: String?](./playerid.md)
  A unique identifier for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkbaseplayer/displayname)*