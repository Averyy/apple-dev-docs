# removeAllRules()

**Framework**: GameplayKit  
**Kind**: method

Removes all rules from the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllRules()
```

#### Discussion

Calling this method also empties the [`agenda`](gkrulesystem/agenda.md) and [`executed`](gkrulesystem/executed.md) arrays.

## See Also

- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [var executed: [GKRule]](gkrulesystem/executed.md)
  The list of rules whose actions have been performed during evaluation of the system.
- [var rules: [GKRule]](gkrulesystem/rules.md)
  The list of rules to be executed when evaluating the system.
- [func add(GKRule)](gkrulesystem/add(_:)-76jb5.md)
  Adds the specified rule to the system.
- [func add([GKRule])](gkrulesystem/add(_:)-7u5zw.md)
  Adds the specified list of rules to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/removeallrules())*