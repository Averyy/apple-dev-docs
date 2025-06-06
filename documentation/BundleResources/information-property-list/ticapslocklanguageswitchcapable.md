# TICapsLockLanguageSwitchCapable

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that enables the Caps Lock key to switch between Latin and non-Latin input sources.

**Availability**:
- macOS 10.15+

#### Discussion

Latin input sources, such as ABC, U.S., and Vietnamese, output characters in Latin script. Non-Latin input sources, such as Bulgarian (Cyrillic script), Hindi (Devanagari script), and Urdu (Arabic script), output characters in scripts other than Latin.

After implementing the key, users can enable or disable this functionality by modifying the “Use Caps Lock to switch to and from” preference, which can be found in System Preferences > Keyboard > Input Sources.

## See Also

- [CFBundleDevelopmentRegion](information-property-list/cfbundledevelopmentregion.md)
  The default language and region for the bundle, as a language ID.
- [CFBundleLocalizations](information-property-list/cfbundlelocalizations.md)
  The localizations handled manually by your app.
- [CFBundleAllowMixedLocalizations](information-property-list/cfbundleallowmixedlocalizations.md)
  A Boolean value that indicates whether the bundle supports the retrieval of localized strings from frameworks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/ticapslocklanguageswitchcapable)*