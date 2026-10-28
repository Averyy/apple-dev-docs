# allowedMenuItemsForLanguageIdentifier:

**Framework**: Automatic Assessment Configuration  
**Kind**: method  
**Role**: Instance Method

Returns the set of allowed menu item titles for the given language identifier, or `nil` if no items have been configured for that identifier.

**Availability**:
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
- (NSSet<NSString *> *) allowedMenuItemsForLanguageIdentifier:(NSString *) languageIdentifier;
```

## Discussion

Menu item titles are matched against the participant application’s localized menu items at the time the assessment session begins. The system resolves each language identifier to the best-matching localization the application bundle provides, so an exact locale match is not required.

## Parameters

- `languageIdentifier`: A BCP 47 language identifier (for example, `en` or `zh-Hans`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/allowedmenuitemsforlanguageidentifier:)*