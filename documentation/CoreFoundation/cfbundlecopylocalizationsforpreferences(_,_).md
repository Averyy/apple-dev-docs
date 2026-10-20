# CFBundleCopyLocalizationsForPreferences(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Given an array of possible localizations and preferred locations, returns the one or more of them that CFBundle would use, without reference to the current application context.

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
func CFBundleCopyLocalizationsForPreferences(_ locArray: CFArray!, _ prefArray: CFArray!) -> CFArray!
```

```c
extern CFArrayRefCFBundleCopyLocalizationsForPreferences(CFArrayRef locArray, CFArrayRef prefArray);
```

#### Return Value

An array containing the localizations that CFBundle would use. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This is not the same as [`CFBundleCopyPreferredLocalizationsFromArray(_:)`](./cfbundlecopypreferredlocalizationsfromarray%28_%29.md), because that function takes the current application context into account. To determine the localizations that another application would use, apply this function to the result of [`CFBundleCopyBundleLocalizations(_:)`](./cfbundlecopybundlelocalizations%28_%29.md).

## Parameters

- `locArray`: An array of possible localizations to search.
- `prefArray`: An array of preferred localizations. If `NULL`, the user’s actual preferred localizations will be used.

## See Also

### Managing Localizations
- [func CFBundleCopyBundleLocalizations(CFBundle!) -> CFArray!](./cfbundlecopybundlelocalizations%28_%29.md)
  Returns an array containing a bundle’s localizations.
- [func CFBundleCopyLocalizedString(CFBundle!, CFString!, CFString!, CFString!) -> CFString!](./cfbundlecopylocalizedstring%28_,_,_,_%29.md)
  Returns a localized string from a bundle’s strings file.
- [func CFBundleCopyLocalizationsForURL(CFURL!) -> CFArray!](./cfbundlecopylocalizationsforurl%28_%29.md)
  Returns an array containing the localizations for a bundle or executable at a particular location.
- [func CFBundleCopyPreferredLocalizationsFromArray(CFArray!) -> CFArray!](./cfbundlecopypreferredlocalizationsfromarray%28_%29.md)
  Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopylocalizationsforpreferences(_:_:))*