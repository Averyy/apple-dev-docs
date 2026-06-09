# setAllowedMenuItems(_:for:)

**Framework**: Automatic Assessment Configuration  
**Kind**: method

Sets the allowed menu item titles for the given language.

**Availability**:
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
func setAllowedMenuItems(_ menuItems: Set<String>?, for language: Locale.Language)
```

#### Discussion

Use this method to specify which menu items the participant application may display during an assessment session. Titles must match the application’s localized menu item strings for the corresponding language.

If multiple languages resolve to the same application localization, the system combines their sets of allowed menu items.

## Parameters

- `menuItems`: The set of menu item titles to allow, or `nil` to remove the entry for `language`.
- `language`: The language to associate with `menuItems`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentparticipantconfiguration/setallowedmenuitems(_:for:))*