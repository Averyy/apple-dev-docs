# NEFilterSettings

**Framework**: Network Extension  
**Kind**: class

The rules and other settings that define the operation of a filter.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NEFilterSettings
```

#### Overview

[`NEFilterDataProvider`](nefilterdataprovider.md) instances use [`NEFilterSettings`](nefiltersettings.md) to communicate the desired settings for the filter to the framework. The framework takes care of applying the contained settings to the system.

## Topics

### Creating Filter Settings
- [init(rules: [NEFilterRule], defaultAction: NEFilterAction)](nefiltersettings/init(rules:defaultaction:).md)
  Creates a new settings instance from an array of rules and a default action.
- [class NEFilterRule](nefilterrule.md)
  A rule for filters that combines a rule to match network traffic and an action to take when the rule matches.
### Inspecting Filter Settings
- [var rules: [NEFilterRule]](nefiltersettings/rules.md)
  An ordered list of rules that define the filter’s operation.
- [var defaultAction: NEFilterAction](nefiltersettings/defaultaction.md)
  The default action to take for flows of network data that don’t match any of the specified rules.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func apply(NEFilterSettings?, completionHandler: ((any Error)?) -> Void)](nefilterdataprovider/apply(_:completionhandler:).md)
  Applies a set of filtering rules associated with the provider and changes the default filtering action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersettings)*