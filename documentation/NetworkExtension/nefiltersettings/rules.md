# rules

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An ordered list of rules that define the filter’s operation.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var rules: [NEFilterRule] { get }
```

```objc
@property (copy, readonly) NSArray<NEFilterRule *> * rules;
```

## Discussion

After applying the [`NEFilterSettings`](../nefiltersettings.md), the system compares each network flow against these rules in order, and acts on the rule of the first [`NEFilterAction`](../nefilteraction.md) that matches.

## See Also

### Inspecting Filter Settings
- [var defaultAction: NEFilterAction](./defaultaction.md)
  The default action to take for flows of network data that don’t match any of the specified rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersettings/rules)*