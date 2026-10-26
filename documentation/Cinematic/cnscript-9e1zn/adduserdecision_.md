# addUserDecision:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Adds a new user decision, and replaces an existing user decision if the times are identical.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (BOOL) addUserDecision:(CNDecision *) decision;
```

#### Return Value

A flag indicating whether adding the user decision was successful.

#### Discussion

> **Note**:  Adding a decision can fail if the decision focuses on a detection or group that does not exist or if its time is not within the time range of the Cinematic script.

## Parameters

- `decision`: The decision to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-9e1zn/adduserdecision:)*