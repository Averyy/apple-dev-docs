# preferredLanguages

**Framework**: Foundation  
**Kind**: property

An ordered list of the user’s preferred languages.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var preferredLanguages: [String] { get }
```

#### Discussion

Users choose a primary language when configuring a device, as described in [`Reviewing Language and Region Settings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/SpecifyingPreferences/SpecifyingPreferences.html#//apple_ref/doc/uid/10000171i-CH12). They may also specify one or more secondary languages in order of preference for use when localization is unavailable in a higher priority language. Use this property to obtain the current user’s ordered list of languages, presented as an array of locale identifier strings.

For more information about language localization in your app, see [`Language and Locale IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/preferredlanguages)*