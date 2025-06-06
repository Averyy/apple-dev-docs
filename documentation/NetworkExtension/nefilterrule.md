# NEFilterRule

**Framework**: Network Extension  
**Kind**: class

A rule for filters that combines a rule to match network traffic and an action to take when the rule matches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterRule
```

## Topics

### Creating a Filter Rule
- [init(networkRule: NENetworkRule, action: NEFilterAction)](nefilterrule/init(networkrule:action:).md)
  Creates a new filter rule from a network rule and an action to take when network traffic matches.
### Inspecting Filter Rule Properties
- [var networkRule: NENetworkRule](nefilterrule/networkrule.md)
  The network rule that defines the network traffic characteristics that this filter rule matches.
- [var action: NEFilterAction](nefilterrule/action.md)
  The action to take when this rule matches network traffic.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [init(rules: [NEFilterRule], defaultAction: NEFilterAction)](nefiltersettings/init(rules:defaultaction:).md)
  Creates a new settings instance from an array of rules and a default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterrule)*