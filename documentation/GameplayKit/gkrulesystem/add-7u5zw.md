# add(_:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified list of rules to the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ rules: [GKRule])
```

#### Discussion

Adding rules to the system also adds them to the [`agenda`](gkrulesystem/agenda.md) list, in decreasing order of the rules’ [`salience`](gkrule/salience.md) values. Rules with the same salience are added to the agenda in the order of the specified array.

## Parameters

- `rules`: An array of rule objects.

## See Also

- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [var rules: [GKRule]](gkrulesystem/rules.md)
  The list of rules to be executed when evaluating the system.
- [func add(GKRule)](gkrulesystem/add(_:)-76jb5.md)
  Adds the specified rule to the system.
- [func removeAllRules()](gkrulesystem/removeallrules.md)
  Removes all rules from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/add(_:)-7u5zw)*