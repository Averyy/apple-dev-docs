# groupIdentifier

**Framework**: GameKit  
**Kind**: property

The identifier for the group that the achievement description is part of.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var groupIdentifier: String? { get }
```

#### Discussion

If your game is configured to be part of a game group in App Store Connect, this property holds the identifier you assigned to the achievement in the game group. If the game isn’t part of a game group, this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementdescription/groupidentifier)*