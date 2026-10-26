# getLocallyAvailableLanguagesWithCompletionHandler:

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Gets the languages used by asset packs that are localized and are available locally.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) getLocallyAvailableLanguagesWithCompletionHandler:(void (^)(NSArray<NSString *> *languageIdentifiers)) completionHandler;
```

## Parameters

- `completionHandler`: A block that receives an array of BCP-47 language identifiers.

## See Also

### Inspecting language support
- [resolvedLanguage](./resolvedlanguage.md)
  The language asset packs that are localized for which the system automatically makes available locally, represented as a BCP-47 identifier.
- [- reconcilePreferredLanguagesWithCompletionHandler:](./reconcilepreferredlanguageswithcompletionhandler_.md)
  Reconciles the set of locally available asset packs with the current preferred languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/getlocallyavailablelanguageswithcompletionhandler:)*