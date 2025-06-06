# removeUserDecision(_:)

**Framework**: Cinematic  
**Kind**: method

Removes an existing user decision.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func removeUserDecision(_ decision: CNDecision) -> Bool
```

#### Return Value

A flag indicating whether the user decisions was removed.

#### Discussion

You can’t remove decisions that aren’t user decisions.

## Parameters

- `decision`: The user decision added to the script or one made at recording time by tapping on the script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/removeuserdecision(_:))*