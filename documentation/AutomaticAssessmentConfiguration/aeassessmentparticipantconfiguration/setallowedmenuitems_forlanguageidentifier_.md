# setAllowedMenuItems:forLanguageIdentifier:

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

Sets the allowed menu item titles for the given language identifier.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
- (void) setAllowedMenuItems:(NSSet<NSString *> *) menuItems forLanguageIdentifier:(NSString *) languageIdentifier;
```

## Discussion

Titles must match the participant application’s localized menu item strings for the corresponding language. If multiple language identifiers resolve to the same application localization, the system combines their sets of allowed menu items.

## Parameters

- `menuItems`: The set of menu item titles to allow, or `nil` to remove the entry for `languageIdentifier`.
- `languageIdentifier`: A BCP 47 language identifier (for example, `en` or `zh-Hans`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/setallowedmenuitems:forlanguageidentifier:)*