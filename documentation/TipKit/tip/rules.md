# rules

**Framework**: TipKit  
**Kind**: property  
**Required**: Yes

The rules that determine when a tip is eligible for display. For more information on rules, see [`Rule`](tips/rule.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@Tips
.RuleBuilder var rules: [Self.Rule] { get }
```

#### Discussion

Use this property to define the rules for when your tips display. If you don’t supply a value, this property returns an empty array of type `Rule`.

## See Also

- [typealias Rule](tip/rule.md)
  A condition to meet before displaying a tip.
- [typealias Event](tip/event.md)
  A repeatable user-defined action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tip/rules)*