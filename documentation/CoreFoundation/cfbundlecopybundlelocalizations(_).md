# CFBundleCopyBundleLocalizations(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns an array containing a bundle’s localizations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFBundleCopyBundleLocalizations(_ bundle: CFBundle!) -> CFArray!
```

#### Return Value

An array containing `bundle`’s localizations. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The array returned by this function is typically passed as a parameter to either the [`CFBundleCopyPreferredLocalizationsFromArray(_:)`](cfbundlecopypreferredlocalizationsfromarray(_:).md) or [`CFBundleCopyLocalizationsForPreferences(_:_:)`](cfbundlecopylocalizationsforpreferences(_:_:).md) function.

## Parameters

- `bundle`: The bundle to examine.

## See Also

- [func CFBundleCopyLocalizedString(CFBundle!, CFString!, CFString!, CFString!) -> CFString!](cfbundlecopylocalizedstring(_:_:_:_:).md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleCopyLocalizationsForPreferences(CFArray!, CFArray!) -> CFArray!](cfbundlecopylocalizationsforpreferences(_:_:).md)
  Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [func CFBundleCopyLocalizationsForURL(CFURL!) -> CFArray!](cfbundlecopylocalizationsforurl(_:).md)
  Returns an array containing the localizations for a bundle or executable at a particular location.
- [func CFBundleCopyPreferredLocalizationsFromArray(CFArray!) -> CFArray!](cfbundlecopypreferredlocalizationsfromarray(_:).md)
  Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopybundlelocalizations(_:))*