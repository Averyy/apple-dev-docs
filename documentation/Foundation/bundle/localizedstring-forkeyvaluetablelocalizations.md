# localizedString(forKey:value:table:localizations:)

**Framework**: Foundation  
**Kind**: method

Look up a localized string given a list of available languages.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func localizedString(forKey key: String, value: String?, table tableName: String?, localizations: [Locale.Language]) -> String
```

#### Return Value

A localized version of the string designated by `key` in table `tableName`.

## Parameters

- `key`: The key for the localized string to retrieve.
- `value`: A default value to return if a localized string for   cannot be found.
- `tableName`: The name of the strings file to search. If  , the method uses tables in  .
- `localizations`: An array of   corresponding to available localizations. Bundle compares the array against its available localizations, and uses the best result to retrieve the localized string. If empty, we treat it as no localization is available, and may return a fallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/localizedstring(forkey:value:table:localizations:))*