# NEOnDemandRuleDisconnect

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A VPN On Demand rule that disconnects the VPN.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEOnDemandRuleDisconnect
```

```objc
@interface NEOnDemandRuleDisconnect : NEOnDemandRule
```

## Overview

When rules of this class match, the VPN connection is not started, and the VPN connection is disconnected if it is not already disconnected.

## Relationships

### Inherits From
- [NEOnDemandRule](./neondemandrule.md)
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

### Settings
- [class NEOnDemandRuleConnect](./neondemandruleconnect.md)
  A VPN On Demand rule that connects the VPN.
- [class NEOnDemandRuleIgnore](./neondemandruleignore.md)
  A VPN On Demand rule that doesn’t change the status of the VPN.
- [class NEOnDemandRuleEvaluateConnection](./neondemandruleevaluateconnection.md)
  A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.
- [class NEOnDemandRule](./neondemandrule.md)
  A base class shared by all VPN On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruledisconnect)*