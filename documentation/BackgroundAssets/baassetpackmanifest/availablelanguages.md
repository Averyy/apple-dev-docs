# availableLanguages

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The languages, represented as their respective BCP-47 identifiers, for which asset packs in this manifest are localized.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (copy, readonly) NSArray<NSString *> * availableLanguages;
```

## See Also

### Inspecting asset pack localization
- [primaryLanguage](./primarylanguage.md)
  The application’s primary language, represented as a BCP-47 identifier, as configured in App Store Connect.
- [resolvedLanguage](./resolvedlanguage.md)
  The language, represented as a BCP-47 identifier, asset packs in this manifest that are localized for which the system automatically makes available locally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanifest/availablelanguages)*