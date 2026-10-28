# removeUserDecision:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Removes an existing user decision.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (BOOL) removeUserDecision:(CNDecision *) decision;
```

## Return Value

A flag indicating whether the user decisions was removed.

## Discussion

You can’t remove decisions that aren’t user decisions.

## Parameters

- `decision`: The user decision added to the script or one made at recording time by tapping on the script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/removeuserdecision:)*