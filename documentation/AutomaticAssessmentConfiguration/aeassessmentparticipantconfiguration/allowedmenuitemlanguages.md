# allowedMenuItemLanguages

**Framework**: Automatic Assessment Configuration  
**Kind**: property

The set of languages for which allowed menu items have been configured.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var allowedMenuItemLanguages: Set<Locale.Language> { get }
```

#### Discussion

Contains only languages explicitly added via [`setAllowedMenuItems(_:for:)`](aeassessmentparticipantconfiguration/setallowedmenuitems(_:for:).md). Each returned language matches the value originally passed to that method. Does not include languages inferred through localization resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/allowedmenuitemlanguages)*