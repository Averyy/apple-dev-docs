# CTGetCoreTextVersion()

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Returns the version of the Core Text framework.

**Availability**:
- iOS 3.2+ - Deprecated in 14.0
- iPadOS 3.2+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.5+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Use -[NSProcessInfo operatingSystemVersion]

## Declaration

```swift
func CTGetCoreTextVersion() -> UInt32
```

```c
extern uint32_t CTGetCoreTextVersion();
```

## Return Value

The version number. This value is for comparison with the constants listed in `Core Text Framework Version Numbers`.

## Discussion

This function returns a number indicating the version of the Core Text framework. Note that framework version is not always an accurate indicator of feature availability. The recommended way to use this function is first to check that the function pointer is non-null, followed by calling it and comparing its result to a defined constant (or constants). For example, to determine whether the CoreText API is available:

```objc
if (&CTGetCoreTextVersion != NULL && CTGetCoreTextVersion() >= kCTVersionNumber10_5) {
 // CoreText API is available
}
```

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctgetcoretextversion())*