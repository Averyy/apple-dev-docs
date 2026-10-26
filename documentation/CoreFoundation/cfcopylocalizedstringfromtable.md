# CFCopyLocalizedStringFromTable

**Framework**: Core Foundation  
**Kind**: macro  
**Role**: Macro

Searches the specified strings file for the string associated with the specified key.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define CFCopyLocalizedStringFromTable(key, tbl, comment)
```

#### Return Value

The localized version of the requested string, or `key` if no value corresponding to `key` is found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This is a macro variant of [`CFBundleCopyLocalizedString(_:_:_:_:)`](./cfbundlecopylocalizedstring%28_,_,_,_%29.md) for use with the `genstrings` tool.

## Parameters

- `key`: The development language version of the string. This string is used as the search key to locate the localized version of the string.
- `tbl`: The name of the strings file to search. The name should not include the `strings` filename extension. The case of the string must match that of the file name, even on file systems (such as HFS+) that are not case sensitive with regards to file names
- `comment`: A comment to provide the translators with contextual information necessary for proper translation.

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
- [func CFBundleCopyPreferredLocalizationsFromArray(CFArray!) -> CFArray!](./cfbundlecopypreferredlocalizationsfromarray%28_%29.md)
  Given an array of possible localizations, returns the one or more of them that CFBundle would use in the current application context.
- [CFCopyLocalizedString](./cfcopylocalizedstring.md)
  Searches the default strings file `Localizable.strings` for the string associated with the specified key.
- [CFCopyLocalizedStringFromTableInBundle](./cfcopylocalizedstringfromtableinbundle.md)
  Returns a localized version of the specified string.
- [CFCopyLocalizedStringWithDefaultValue](./cfcopylocalizedstringwithdefaultvalue.md)
  Returns a localized version of a localization string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcopylocalizedstringfromtable)*