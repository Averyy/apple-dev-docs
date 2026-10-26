# resolvedLanguage

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The language, represented as a BCP-47 identifier, asset packs in this manifest that are localized for which the system automatically makes available locally.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (copy, readonly, nullable) NSString * resolvedLanguage;
```

#### Discussion

The user’s preferred languages inform the choice of resolved language, respecting any language that your application sets manually by setting [`resolvedLanguage`](../baassetpackmanager/resolvedlanguage.md). This property may be `nil` if no localized asset packs are available. If the user recently changed their preferred language or if this manifest is outdated, this property’s value may be out of sync with the set of asset packs available locally.

## See Also

### Inspecting asset pack localization
- [primaryLanguage](./primarylanguage.md)
  The application’s primary language, represented as a BCP-47 identifier, as configured in App Store Connect.
- [availableLanguages](./availablelanguages.md)
  The languages, represented as their respective BCP-47 identifiers, for which asset packs in this manifest are localized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/resolvedlanguage)*