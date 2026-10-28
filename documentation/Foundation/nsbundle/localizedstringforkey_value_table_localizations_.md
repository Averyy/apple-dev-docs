# localizedStringForKey:value:table:localizations:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Look up a localized string given a list of available localizations.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```objc
- (NSString *) localizedStringForKey:(NSString *) key value:(NSString *) value table:(NSString *) tableName localizations:(NSArray<NSString *> *) localizations;
```

## Return Value

A localized version of the string designated by `key` in table `tableName`.

## Parameters

- `key`: The key for the localized string to retrieve.
- `value`: A default value to return if a localized string for `key` cannot be found.
- `tableName`: The name of the strings file to search. If `nil`, the method uses tables in `Localizable.strings`.
- `localizations`: An array of BCP 47 language codes corresponding to available localizations. Bundle compares the array against its available localizations, and uses the best result to retrieve the localized string. If empty, we treat it as no localization is available, and may return a fallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundle/localizedstringforkey:value:table:localizations:)*