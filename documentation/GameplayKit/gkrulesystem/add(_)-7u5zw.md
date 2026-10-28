# add(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addRulesFromArray:(NSArray<GKRule *> *) rules;
```

## Discussion

Adding rules to the system also adds them to the [`agenda`](./agenda.md) list, in decreasing order of the rules’ [`salience`](../gkrule/salience.md) values. Rules with the same salience are added to the agenda in the order of the specified array.

## Parameters

- `rules`: An array of rule objects.

## See Also

### Related Documentation
- [var agenda: [GKRule]](./agenda.md)
  The list of rules to be considered when evaluating the system.
### Managing a System’s List of Rules
- [var rules: [GKRule]](./rules.md)
  The list of rules to be executed when evaluating the system.
- [func add(GKRule)](./add%28_%29-76jb5.md)
  Adds the specified rule to the system.
- [func removeAllRules()](./removeallrules%28%29.md)
  Removes all rules from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/add(_:)-7u5zw)*