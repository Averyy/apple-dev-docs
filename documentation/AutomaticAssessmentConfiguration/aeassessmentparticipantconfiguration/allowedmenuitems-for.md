# allowedMenuItems(for:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Returns the set of allowed menu item titles for the given language, or `nil` if no items have been configured for that language.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
func allowedMenuItems(for language: Locale.Language) -> Set<String>?
```

#### Discussion

Menu item titles are matched against the participant application’s localized menu items at the time the assessment session begins. The system resolves each language to the best-matching localization the application bundle provides, so an exact locale match is not required.

## Parameters

- `language`: The language for which to return allowed menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/allowedmenuitems(for:))*