# CTFontManagerSetAutoActivationSetting(_:_:)

**Framework**: Core Text  
**Kind**: func

Sets the auto-activation setting for the specified bundle identifier.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func CTFontManagerSetAutoActivationSetting(_ bundleIdentifier: CFString?, _ setting: CTFontManagerAutoActivationSetting)
```

## Parameters

- `bundleIdentifier`: The bundle identifier used to specify a particular application bundle. If  , the current application bundle is used. If   is specified, sets global auto-activation.
- `setting`: The new setting. See   for possible values.

## See Also

- [func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(CFArray, CFSet?, CTFontDescriptorProgressHandler) -> Bool](ctfontdescriptormatchfontdescriptorswithprogresshandler(_:_:_:).md)
  Matches font descriptors and tracks progress with a progress handler.
- [func CTFontManagerCompareFontFamilyNames(UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer?) -> CFComparisonResult](ctfontmanagercomparefontfamilynames(_:_:_:).md)
  A comparator function to compare font family names and sort them according to Apple guidelines.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagersetautoactivationsetting(_:_:))*