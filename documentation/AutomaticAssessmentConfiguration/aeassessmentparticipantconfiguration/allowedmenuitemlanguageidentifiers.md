# allowedMenuItemLanguageIdentifiers

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The set of language identifiers for which allowed menu items have been configured.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSSet<NSString *> * allowedMenuItemLanguageIdentifiers;
```

## Discussion

Contains only identifiers explicitly added via `setAllowedMenuItems(_:forLanguageIdentifier:)`. Does not include identifiers inferred through localization resolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/allowedmenuitemlanguageidentifiers)*