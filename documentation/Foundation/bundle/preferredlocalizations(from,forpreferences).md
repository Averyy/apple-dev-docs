# preferredLocalizations(from:forPreferences:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.

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
class func preferredLocalizations(from localizationsArray: [String], forPreferences preferencesArray: [String]?) -> [String]
```

```objc
+ (NSArray<NSString *> *) preferredLocalizationsFromArray:(NSArray<NSString *> *) localizationsArray forPreferences:(NSArray<NSString *> *) preferencesArray;
```

#### Return Value

An array of locale identifiers, ordered according to user preference.  If none of the user-preferred localizations are available, this method returns one of the values in `localizationsArray`.

#### Discussion

This method returns only the locale identifiers for which a bundle would  provide localized content. Typically, this means one of the following:

- A single localization that isn’t region-specific
- A region-specific localization, followed by a corresponding localization that isn’t region-specific, as a fallback

This method doesn’t return all localizations in order of user preference. To get this information, you can call this method repeatedly, each time removing the identifiers returned by the previous call.

## Parameters

- `localizationsArray`: An array of identifiers, each corresponding to a localization that a bundle can support.
- `preferencesArray`: An array of BCP 47 language codes corresponding to a user’s preferred languages.

  If this parameter is `nil`, the method uses the current user’s language preferences.

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
- [class func preferredLocalizations(from: [String]) -> [String]](./preferredlocalizations%28from%29.md)
  Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/preferredlocalizations(from:forpreferences:))*