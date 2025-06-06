# init(rules:defaultAction:)

**Framework**: Network Extension  
**Kind**: init

Creates a new settings instance from an array of rules and a default action.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(rules: [NEFilterRule], defaultAction: NEFilterAction)
```

## Parameters

- `rules`: An array containing an ordered list of   objects. The maximum number of rules that this array can contain is 1000.
- `defaultAction`: The   to take for flows of network data that don’t match any of the specified rules. The default   is  . If   is   or  , then the   array must contain at least one  .

## See Also

- [class NEFilterRule](nefilterrule.md)
  A rule for filters that combines a rule to match network traffic and an action to take when the rule matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersettings/init(rules:defaultaction:))*