# NEOnDemandRuleConnect

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A VPN On Demand rule that connects the VPN.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEOnDemandRuleConnect
```

```objc
@interface NEOnDemandRuleConnect : NEOnDemandRule
```

## Overview

When rules of this class match, the system starts the VPN connection whenever an application running on the system opens a network connection.

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
- [class NEOnDemandRuleDisconnect](./neondemandruledisconnect.md)
  A VPN On Demand rule that disconnects the VPN.
- [class NEOnDemandRuleIgnore](./neondemandruleignore.md)
  A VPN On Demand rule that doesn’t change the status of the VPN.
- [class NEOnDemandRuleEvaluateConnection](./neondemandruleevaluateconnection.md)
  A VPN On Demand rule that evaluate the app’s connection to determine whether to run its action.
- [class NEOnDemandRule](./neondemandrule.md)
  A base class shared by all VPN On Demand rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neondemandruleconnect)*