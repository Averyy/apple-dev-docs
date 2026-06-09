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

By default, all Apple menu items are restricted during an assessment. Use this property to specify which menu items should be accessible.

> **Note**: [`aboutThisMac`](aeapplemenuitem/aboutthismac.md) is always visible during assessment sessions regardless of configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowedapplemenuitems)*