# networkRule

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The network rule that defines the network traffic characteristics that this filter rule matches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@NSCopying
var networkRule: NENetworkRule { get }
```

```objc
@property (copy, readonly) NENetworkRule * networkRule;
```

## See Also

### Inspecting Filter Rule Properties
- [var action: NEFilterAction](./action.md)
  The action to take when this rule matches network traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterrule/networkrule)*