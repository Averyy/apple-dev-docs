# retractFact(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified fact from the fact set, and reevaluates the rules in the system’s agenda.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func retractFact(_ fact: any NSObjectProtocol)
```

```objc
- (void) retractFact:(id<NSObject>) fact;
```

## Discussion

Calling this method is equivalent to calling the [`retractFact(_:grade:)`](./retractfact%28_,grade%29.md) method with a `grade` value of 1.0, thus reducing the fact’s membership grade to zero and removing it from the [`facts`](./facts.md) array.

Upon asserting or retracting any facts, the system reevaluates the rules in its [`agenda`](./agenda.md) list so any rules that depend on changes to the set of facts can perform their actions.

## Parameters

- `fact`: An object representing a truth to be rejected by the rule system. For details, see the [`facts`](./facts.md) property.

## See Also

### Asserting and Retracting Facts
- [var facts: [Any]](./facts.md)
  The list of facts claimed by the rule system.
- [func assertFact(any NSObjectProtocol)](./assertfact%28_%29.md)
  Adds the specified fact to the fact set with a membership grade of 1.0, and reevaluates the rules in the system’s agenda.
- [func assertFact(any NSObjectProtocol, grade: Float)](./assertfact%28_,grade%29.md)
  Increases the membership grade of the specified fact by the specified amount, adding it to the fact set if necessary, and reevaluates the rules in the system’s agenda.
- [func retractFact(any NSObjectProtocol, grade: Float)](./retractfact%28_,grade%29.md)
  Reduces the membership grade of the specified fact by the specified amount, removing it from the fact set if necessary, and reevaluates the rules in the system’s agenda.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/retractfact(_:))*