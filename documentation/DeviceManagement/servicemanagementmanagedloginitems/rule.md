# ServiceManagementManagedLoginItems.Rule

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that configures a service management rule.

**Availability**:
- macOS 13.0+

## Declaration

```swift
object ServiceManagementManagedLoginItems.Rule
```

## Properties

- `Comment` (string): An optional description of the rule.
- `RuleType` (string) *(required)*: The type of comparison to make.
- `RuleValue` (string) *(required)*: The value to compare with each login item’s value, to determine if this rule is a match.
- `TeamIdentifier` (string): An additional constraint to limit the scope of the rule that the system tests after matching the `RuleType` and `RuleValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicemanagementmanagedloginitems/rule)*