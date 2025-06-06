# rules

**Framework**: Network Extension  
**Kind**: property

An ordered list of rules that define the filter’s operation.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var rules: [NEFilterRule] { get }
```

#### Discussion

After applying the [`NEFilterSettings`](nefiltersettings.md), the system compares each network flow against these rules in order, and acts on the rule of the first [`NEFilterAction`](nefilteraction.md) that matches.

## See Also

- [var defaultAction: NEFilterAction](nefiltersettings/defaultaction.md)
  The default action to take for flows of network data that don’t match any of the specified rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersettings/rules)*