# addUserDecision(_:)

**Framework**: Cinematic  
**Kind**: method

Adds a new user decision, and replaces an existing user decision if the times are identical.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
final func addUserDecision(_ decision: CNDecision) -> Bool
```

#### Return Value

A flag indicating whether adding a user decision was successful.

#### Discussion

> **Note**:  Adding a decision can fail if the decision focuses on a detection or detection group that does not exist or if its time is not within the time range of the Cinematic script.

## Parameters

- `decision`: The decision to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/adduserdecision(_:))*