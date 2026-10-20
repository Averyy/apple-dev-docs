# removeAllRules()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeAllRules;
```

#### Discussion

Calling this method also empties the [`agenda`](./agenda.md) and [`executed`](./executed.md) arrays.

## See Also

### Related Documentation
- [var agenda: [GKRule]](./agenda.md)
  The list of rules to be considered when evaluating the system.
- [var executed: [GKRule]](./executed.md)
  The list of rules whose actions have been performed during evaluation of the system.
### Managing a System’s List of Rules
- [var rules: [GKRule]](./rules.md)
  The list of rules to be executed when evaluating the system.
- [func add(GKRule)](./add%28_%29-76jb5.md)
  Adds the specified rule to the system.
- [func add([GKRule])](./add%28_%29-7u5zw.md)
  Adds the specified list of rules to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/removeallrules())*