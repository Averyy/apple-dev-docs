# delegate

**Framework**: GameKit  
**Kind**: property

The delegate that handles communication between players in a match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any GKMatchDelegate)? { get set }
```

#### Discussion

To receive voice or data from other players, you must set the delegate.

## See Also

- [protocol GKMatchDelegate](gkmatchdelegate.md)
  An object that receives connection status and data transmitted in a multiplayer game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/delegate)*