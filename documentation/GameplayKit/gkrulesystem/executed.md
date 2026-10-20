# executed

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The list of rules whose actions have been performed during evaluation of the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var executed: [GKRule] { get }
```

```objc
@property (nonatomic, retain, readonly) NSArray<GKRule *> * executed;
```

#### Discussion

When you call the [`evaluate()`](./evaluate%28%29.md) method, the system considers each rule in the [`agenda`](./agenda.md) list in order. If a rule on the agenda is satisfied—that is, its predicate returns [`true`](../../Swift/true.md) and it executes its action—the system moves that rule to the [`executed`](./executed.md) list.

## See Also

### Related Documentation
- [var rules: [GKRule]](./rules.md)
  The list of rules to be executed when evaluating the system.
### Evaluating a Rule System
- [func evaluate()](./evaluate%28%29.md)
  Evaluates the rule system, executing the list of rules in its agenda.
- [var agenda: [GKRule]](./agenda.md)
  The list of rules to be considered when evaluating the system.
- [func reset()](./reset%28%29.md)
  Returns the rule system to its original agenda and clears all facts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/executed)*