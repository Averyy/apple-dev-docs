# challengeEventHandler

**Framework**: GameKit  
**Kind**: method  
**Role**: Type Method

Returns the shared instance of the event handler

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```objc
+ (GKChallengeEventHandler *) challengeEventHandler;
```

#### Return Value

An event handler object.

#### Discussion

Your game never directly creates a [`GKChallengeEventHandler`](../gkchallengeeventhandler.md) object. Instead, retrieve the shared instance using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/challengeeventhandler)*