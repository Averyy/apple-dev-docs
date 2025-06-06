# salience

**Framework**: GameplayKit  
**Kind**: property

The importance of the rule relative to others in a rule system’s agenda.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var salience: Int { get set }
```

#### Discussion

A [`GKRuleSystem`](gkrulesystem.md) object evaluates the rules in its [`agenda`](gkrulesystem/agenda.md) list in order of decreasing salience.

Typically, you set the salience of a rule before calling the [`add(_:)`](gkrulesystem/add(_:)-76jb5.md) or [`add(_:)`](gkrulesystem/add(_:)-7u5zw.md) method, so that the system can insert the new rule into its agenda at the proper position. Changing the salience of a rule already in a rule system does not affect its order in the current agenda, but it does affect the order of the new agenda the rule system builds when you call its [`reset()`](gkrulesystem/reset().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/salience)*