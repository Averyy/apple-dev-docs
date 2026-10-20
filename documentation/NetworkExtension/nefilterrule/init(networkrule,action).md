# init(networkRule:action:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Creates a new filter rule from a network rule and an action to take when network traffic matches.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(networkRule: NENetworkRule, action: NEFilterAction)
```

```objc
- (instancetype) initWithNetworkRule:(NENetworkRule *) networkRule action:(NEFilterAction) action;
```

## Parameters

- `networkRule`: An [`NENetworkRule`](../nenetworkrule.md) object that defines the network traffic characteristics that this rule matches.
- `action`: The action to take when the network rule matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterrule/init(networkrule:action:))*