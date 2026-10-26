# resolvedLanguage

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

The language asset packs that are localized for which the system automatically makes available locally, represented as a BCP-47 identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (copy, readwrite, nullable) NSString * resolvedLanguage;
```

## Mentions

- [Reducing download and storage demands with localized asset packs](../reducing-download-and-storage-demands-with-localized-asset-packs.md)

#### Discussion

The user’s preferred languages inform the choice of resolved language, respecting any language that your application sets manually. This property may be `nil` if no localized asset packs are available. You can manually set this property to `nil` to revert to the user’s system-wide language preference. If the user recently changed their preferred language, then this property’s value could be temporarily out of sync with the set of asset packs that are available locally. Setting the language doesn’t immediately download or remove any asset packs; call [`reconcilePreferredLanguagesWithCompletionHandler:`](./reconcilepreferredlanguageswithcompletionhandler_.md) to reconcile the set of downloaded asset packs with the new configuration.

Setting a new resolved language also changes your application’s display language.

> **Note**: Don’t set this property to a new value within your downloader extension.

## See Also

### Inspecting language support
- [- getLocallyAvailableLanguagesWithCompletionHandler:](./getlocallyavailablelanguageswithcompletionhandler_.md)
  Gets the languages used by asset packs that are localized and are available locally.
- [- reconcilePreferredLanguagesWithCompletionHandler:](./reconcilepreferredlanguageswithcompletionhandler_.md)
  Reconciles the set of locally available asset packs with the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/resolvedlanguage)*