# actionSetType

**Framework**: HomeKit  
**Kind**: property

The type of the action set, such as built-in or user-defined.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actionSetType: String { get }
```

#### Discussion

An action set type can be user-defined, trigger-owned, or one of the built-in types. Note that built-in action sets cannot be removed from the home, and trigger-owned action sets cannot be executed, renamed, or associated with another trigger.

## See Also

- [Action Set Types](action-set-types.md)
  The types of action sets that you can define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmactionset/actionsettype)*