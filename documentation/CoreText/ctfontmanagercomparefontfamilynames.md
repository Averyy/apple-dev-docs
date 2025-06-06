# CTFontManagerCompareFontFamilyNames(_:_:_:)

**Framework**: Core Text  
**Kind**: func

A comparator function to compare font family names and sort them according to Apple guidelines.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func CTFontManagerCompareFontFamilyNames(_ family1: UnsafeRawPointer, _ family2: UnsafeRawPointer, _ context: UnsafeMutableRawPointer?) -> CFComparisonResult
```

#### Return Value

A `CFComparisonResult` value indicating the sort order for the two family names. `kCFComparisonResultGreatherThan` if `family1` is greater than `family2`, `kCFComparisonResultLessThan` if `family1` is less than `family2`, and `kCFComparisonResultEqualTo` if they are equal.

#### Discussion

This `CFComparatorFunction` function compares font family names and sorts them in the Apple preferred order, accounting for foundry prefix. Family names with recognized prefixes are sorted after the unprefixed names in prefix order.

## Parameters

- `family1`: The first localized font family name to compare, as a   object.
- `family2`: The second localized font family name to compare, as a   object.
- `context`: Unused. Can be  .

## See Also

- [func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(CFArray, CFSet?, CTFontDescriptorProgressHandler) -> Bool](ctfontdescriptormatchfontdescriptorswithprogresshandler(_:_:_:).md)
  Matches font descriptors and tracks progress with a progress handler.
- [func CTFontManagerCopyAvailableFontFamilyNames() -> CFArray](ctfontmanagercopyavailablefontfamilynames().md)
  Returns an array of visible font family names sorted for user interface display.
- [func CTFontManagerCopyAvailableFontURLs() -> CFArray](ctfontmanagercopyavailablefonturls().md)
  Returns an array of font URLs.
- [func CTFontManagerCopyAvailablePostScriptNames() -> CFArray](ctfontmanagercopyavailablepostscriptnames().md)
  Returns an array of unique PostScript font names for the fonts.
- [func CTFontManagerCreateFontDescriptorFromData(CFData) -> CTFontDescriptor?](ctfontmanagercreatefontdescriptorfromdata(_:).md)
  Creates a font descriptor representing the font in the supplied data.
- [func CTFontManagerCreateFontDescriptorsFromURL(CFURL) -> CFArray?](ctfontmanagercreatefontdescriptorsfromurl(_:).md)
  Returns an array of font descriptors representing each of the fonts in the specified URL.
- [func CTFontManagerCreateFontRequestRunLoopSource(CFIndex, (CFDictionary, pid_t) -> Unmanaged<CFArray>) -> CFRunLoopSource?](ctfontmanagercreatefontrequestrunloopsource(_:_:).md)
  Creates a reference to a run loop source used to convey font requests from the Font Manager.
- [func CTFontManagerEnableFontDescriptors(CFArray, Bool)](ctfontmanagerenablefontdescriptors(_:_:).md)
  Enables or disables the matching font descriptors for font descriptor matching.
- [func CTFontManagerGetAutoActivationSetting(CFString?) -> CTFontManagerAutoActivationSetting](ctfontmanagergetautoactivationsetting(_:).md)
  Gets the auto-activation setting for the specified bundle identifier.
- [func CTFontManagerGetScopeForURL(CFURL) -> CTFontManagerScope](ctfontmanagergetscopeforurl(_:).md)
  Returns the registration scope of the specified URL.
- [func CTFontManagerIsSupportedFont(CFURL) -> Bool](ctfontmanagerissupportedfont(_:).md)
  Determines whether a file is in a supported font format.
- [func CTFontManagerRegisterFontsForURL(CFURL, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](ctfontmanagerregisterfontsforurl(_:_:_:).md)
  Registers fonts from the specified font URL with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [func CTFontManagerRegisterFontsForURLs(CFArray, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](ctfontmanagerregisterfontsforurls(_:_:_:).md)
  Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [func CTFontManagerRegisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](ctfontmanagerregistergraphicsfont(_:_:).md)
  Registers the specified graphics font with the font manager.
- [func CTFontManagerSetAutoActivationSetting(CFString?, CTFontManagerAutoActivationSetting)](ctfontmanagersetautoactivationsetting(_:_:).md)
  Sets the auto-activation setting for the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagercomparefontfamilynames(_:_:_:))*