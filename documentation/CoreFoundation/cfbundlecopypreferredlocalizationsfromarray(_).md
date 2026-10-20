# CFBundleCopyPreferredLocalizationsFromArray(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBundleCopyPreferredLocalizationsFromArray(_ locArray: CFArray!) -> CFArray!
```

```c
extern CFArrayRefCFBundleCopyPreferredLocalizationsFromArray(CFArrayRef locArray);
```

#### Return Value

A subset of `locArray` that CFBundle would use in the current application context. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You can obtain `locArray` using the [`CFBundleCopyBundleLocalizations(_:)`](./cfbundlecopybundlelocalizations%28_%29.md) function.

## Parameters

- `locArray`: An array of possible localizations.

## See Also

### Managing Localizations
- [func CFBundleCopyBundleLocalizations(CFBundle!) -> CFArray!](./cfbundlecopybundlelocalizations%28_%29.md)
  Returns an array containing a bundle’s localizations.
- [func CFBundleCopyLocalizedString(CFBundle!, CFString!, CFString!, CFString!) -> CFString!](./cfbundlecopylocalizedstring%28_,_,_,_%29.md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleCopyLocalizationsForPreferences(CFArray!, CFArray!) -> CFArray!](./cfbundlecopylocalizationsforpreferences%28_,_%29.md)
  Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.
- [func CFBundleCopyLocalizationsForURL(CFURL!) -> CFArray!](./cfbundlecopylocalizationsforurl%28_%29.md)
  Returns an array containing the localizations for a bundle or executable at a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopypreferredlocalizationsfromarray(_:))*