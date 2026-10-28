# CTFontManagerUnregisterGraphicsFont(_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Unregisters the specified graphics font with the font manager.

**Availability**:
- iOS 4.1+ - Deprecated in 18.0
- iPadOS 4.1+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 2.0+ - Deprecated in 11.0

> **Deprecated**: Use the API corresponding to the one used to register the font

## Declaration

```swift
func CTFontManagerUnregisterGraphicsFont(_ font: CGFont, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

```c
extern bool CTFontManagerUnregisterGraphicsFont(CGFontRef font, CFErrorRef*error);
```

## Return Value

`true` if unregistration of the font was successful, otherwise `false`.

## Discussion

Unregistered fonts are no longer discoverable through font descriptor matching. Fonts that are backed by files should be unregistered using [`CTFontManagerUnregisterFontsForURL(_:_:_:)`](./ctfontmanagerunregisterfontsforurl%28_,_,_%29.md).

## Parameters

- `font`: The graphics font to be unregistered.
- `error`: Returns by indirection an error object in the case of failed unregistration.

## See Also

### Related Documentation
- [func CTFontManagerRegisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerregistergraphicsfont%28_,_%29.md)
  Registers the specified graphics font with the font manager.
### Functions
- [func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(CFArray, CFSet?, CTFontDescriptorProgressHandler) -> Bool](./ctfontdescriptormatchfontdescriptorswithprogresshandler%28_,_,_%29.md)
  Matches font descriptors and tracks progress with a progress handler.
- [func CTFontManagerCompareFontFamilyNames(UnsafeRawPointer, UnsafeRawPointer, UnsafeMutableRawPointer?) -> CFComparisonResult](./ctfontmanagercomparefontfamilynames%28_,_,_%29.md)
  A comparator function to compare font family names and sort them according to Apple guidelines.
- [func CTFontManagerCopyAvailableFontFamilyNames() -> CFArray](./ctfontmanagercopyavailablefontfamilynames%28%29.md)
  Returns an array of visible font family names sorted for user interface display.
- [func CTFontManagerCopyAvailableFontURLs() -> CFArray](./ctfontmanagercopyavailablefonturls%28%29.md)
  Returns an array of font URLs.
- [func CTFontManagerCopyAvailablePostScriptNames() -> CFArray](./ctfontmanagercopyavailablepostscriptnames%28%29.md)
  Returns an array of unique PostScript font names for the fonts.
- [func CTFontManagerCreateFontDescriptorFromData(CFData) -> CTFontDescriptor?](./ctfontmanagercreatefontdescriptorfromdata%28_%29.md)
  Creates a font descriptor representing the font in the supplied data.
- [func CTFontManagerCreateFontDescriptorsFromURL(CFURL) -> CFArray?](./ctfontmanagercreatefontdescriptorsfromurl%28_%29.md)
  Returns an array of font descriptors representing each of the fonts in the specified URL.
- [func CTFontManagerCreateFontRequestRunLoopSource(CFIndex, (CFDictionary, pid_t) -> Unmanaged<CFArray>) -> CFRunLoopSource?](./ctfontmanagercreatefontrequestrunloopsource%28_,_%29.md)
  Creates a reference to a run loop source used to convey font requests from the Font Manager.
- [func CTFontManagerEnableFontDescriptors(CFArray, Bool)](./ctfontmanagerenablefontdescriptors%28_,_%29.md)
  Enables or disables the matching font descriptors for font descriptor matching.
- [func CTFontManagerGetAutoActivationSetting(CFString?) -> CTFontManagerAutoActivationSetting](./ctfontmanagergetautoactivationsetting%28_%29.md)
  Gets the auto-activation setting for the specified bundle identifier.
- [func CTFontManagerGetScopeForURL(CFURL) -> CTFontManagerScope](./ctfontmanagergetscopeforurl%28_%29.md)
  Returns the registration scope of the specified URL.
- [func CTFontManagerIsSupportedFont(CFURL) -> Bool](./ctfontmanagerissupportedfont%28_%29.md)
  Determines whether a file is in a supported font format.
- [func CTFontManagerRegisterFontsForURL(CFURL, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerregisterfontsforurl%28_,_,_%29.md)
  Registers fonts from the specified font URL with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [func CTFontManagerRegisterFontsForURLs(CFArray, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](./ctfontmanagerregisterfontsforurls%28_,_,_%29.md)
  Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [func CTFontManagerRegisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerregistergraphicsfont%28_,_%29.md)
  Registers the specified graphics font with the font manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerunregistergraphicsfont(_:_:))*