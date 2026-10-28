# preferredLocalizations(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func preferredLocalizations(from localizationsArray: [String]) -> [String]
```

```objc
+ (NSArray<NSString *> *) preferredLocalizationsFromArray:(NSArray<NSString *> *) localizationsArray;
```

## Return Value

An array of `NSString` objects containing the preferred localizations. These strings are ordered in the array according to the user’s language preferences and are taken from the strings in the `localizationsArray` parameter.

## Discussion

This method does not return all localizations in preference order but only those from which `NSBundle` would get localized content, typically either a single non-region-specific localization or a region-specific localization followed by a corresponding non-region-specific localization as a fallback.

However, clients who want all localizations in preference order can make repeated calls, each time taking the top localizations out of the list of localizations passed in.

## Parameters

- `localizationsArray`: An array of `NSString` objects, each of which specifies the language ID for a localization that the bundle supports.

## See Also

### Getting localization information
- [var localizations: [String]](./localizations.md)
  A list of all the localizations contained in the bundle.
- [var preferredLocalizations: [String]](./preferredlocalizations.md)
  An ordered list of preferred localizations contained in the bundle.
- [var developmentLocalization: String?](./developmentlocalization.md)
  The localization for the development language.
- [var localizedInfoDictionary: [String : Any]?](./localizedinfodictionary.md)
  A dictionary with the keys from the bundle’s localized property list.
- [class func preferredLocalizations(from: [String], forPreferences: [String]?) -> [String]](./preferredlocalizations%28from,forpreferences%29.md)
  Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/preferredlocalizations(from:))*