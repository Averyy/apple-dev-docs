# allowedAppleMenuItems

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The set of allowed Apple menu items during an assessment.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowedAppleMenuItems: Set<AEAppleMenuItem>? { get set }
```

#### Discussion

Defaults to `nil`, which leaves every Apple menu item available. Setting a non-`nil` set restricts the menu to the items it names; pass an empty set to restrict all of them. Some constants cover more than one menu item.

> **Note**: [`aboutThisMac`](aeapplemenuitem/aboutthismac.md) is always visible during assessment sessions regardless of configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowedapplemenuitems)*