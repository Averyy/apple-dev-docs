# localizedInfoDictionary

**Framework**: Foundation  
**Kind**: property

A dictionary with the keys from the bundle’s localized property list.

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
var localizedInfoDictionary: [String : Any]? { get }
```

#### Discussion

This property uses the preferred localization for the current user when determining which resources to include. If the preferred localization is not available, this property chooses the most appropriate localization found in the bundle.

## See Also

- [var localizations: [String]](bundle/localizations.md)
  A list of all the localizations contained in the bundle.
- [var preferredLocalizations: [String]](bundle/preferredlocalizations.md)
  An ordered list of preferred localizations contained in the bundle.
- [var developmentLocalization: String?](bundle/developmentlocalization.md)
  The localization for the development language.
- [class func preferredLocalizations(from: [String]) -> [String]](bundle/preferredlocalizations(from:).md)
  Returns one or more localizations from the specified list that a bundle object would use to locate resources for the current user.
- [class func preferredLocalizations(from: [String], forPreferences: [String]?) -> [String]](bundle/preferredlocalizations(from:forpreferences:).md)
  Returns locale identifiers for which a bundle would provide localized content, given a specified list of candidates for a user’s language preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/localizedinfodictionary)*