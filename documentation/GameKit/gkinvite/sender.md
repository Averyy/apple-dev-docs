# sender

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The player who sends the invitation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sender: GKPlayer { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain, readonly) GKPlayer * sender;
```

*macOS*

```objc
@property (atomic, retain, readonly) GKPlayer * sender;
```

## See Also

### Getting Properties
- [var playerAttributes: UInt32](./playerattributes.md)
  The player attributes for the match.
- [var playerGroup: Int](./playergroup.md)
  The player group for the match.
- [var isHosted: Bool](./ishosted.md)
  A Boolean value that indicates whether you host the game on your own servers.
- [var inviter: String](./inviter.md)
  The identifier for the player who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkinvite/sender)*