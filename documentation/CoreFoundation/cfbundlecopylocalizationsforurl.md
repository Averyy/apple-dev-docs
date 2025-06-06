# CFBundleCopyLocalizationsForURL(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns an array containing the localizations for a bundle or executable at a particular location.

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
func CFBundleCopyLocalizationsForURL(_ url: CFURL!) -> CFArray!
```

#### Return Value

An array containing the localizations available at `url`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

For a directory URL, this is equivalent to calling the [`CFBundleCopyBundleLocalizations(_:)`](cfbundlecopybundlelocalizations(_:).md) function on the corresponding bundle. For a plain file URL representing an unbundled application, this will attempt to determine its localizations using the [`kCFBundleLocalizationsKey`](kcfbundlelocalizationskey.md) and [`kCFBundleDevelopmentRegionKey`](kcfbundledevelopmentregionkey.md) keys in the dictionary returned by [`CFBundleCopyInfoDictionaryForURL(_:)`](cfbundlecopyinfodictionaryforurl(_:).md), or a `vers` resource if those are not present.

## Parameters

- `url`: The location of a bundle’s localizations.

## See Also

- [func CFBundleCopyBundleLocalizations(CFBundle!) -> CFArray!](cfbundlecopybundlelocalizations(_:).md)
  Returns an array containing a bundle’s localizations.
- [func CFBundleCopyLocalizedString(CFBundle!, CFString!, CFString!, CFString!) -> CFString!](cfbundlecopylocalizedstring(_:_:_:_:).md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleCopyLocalizationsForPreferences(CFArray!, CFArray!) -> CFArray!](cfbundlecopylocalizationsforpreferences(_:_:).md)
  Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [func CFBundleCopyPreferredLocalizationsFromArray(CFArray!) -> CFArray!](cfbundlecopypreferredlocalizationsfromarray(_:).md)
  Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizationsforurl(_:))*