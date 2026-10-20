# trigger(challengeDefinitionID:handler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Displays the challenge creation view for the provided challenge definition ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func trigger(challengeDefinitionID: String, handler: (@Sendable () -> Void)? = nil)
```

```swift
func trigger(challengeDefinitionID: String) async
```

```objc
- (void) triggerAccessPointWithChallengeDefinitionID:(NSString *) challengeDefinitionID handler:(void (^)()) handler;
```

## Mentions

- [Creating engaging challenges from leaderboards](../creating-engaging-challenges-from-leaderboards.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(challengedefinitionid:handler:))*