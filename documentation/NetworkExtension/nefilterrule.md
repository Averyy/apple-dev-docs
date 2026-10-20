# NEFilterRule

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A rule for filters that combines a rule to match network traffic and an action to take when the rule matches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterRule
```

```objc
@interface NEFilterRule : NSObject
```

## Topics

### Creating a Filter Rule
- [init(networkRule: NENetworkRule, action: NEFilterAction)](./nefilterrule/init%28networkrule,action%29.md)
  Creates a new filter rule from a network rule and an action to take when network traffic matches.
### Inspecting Filter Rule Properties
- [var networkRule: NENetworkRule](./nefilterrule/networkrule.md)
  The network rule that defines the network traffic characteristics that this filter rule matches.
- [var action: NEFilterAction](./nefilterrule/action.md)
  The action to take when this rule matches network traffic.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Creating Filter Settings
- [init(rules: [NEFilterRule], defaultAction: NEFilterAction)](./nefiltersettings/init%28rules,defaultaction%29.md)
  Creates a new settings instance from an array of rules and a default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterrule)*