# CTFontManagerRegisterFontsForURLs(_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching.

**Availability**:
- iOS 4.1+ - Deprecated in 13.0 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- iPadOS 4.1+ - Deprecated in 13.0 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- macOS 10.6+ - Deprecated in 10.15 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- tvOS 9.0+ - Deprecated in 13.0 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))
- watchOS 2.0+ - Deprecated in 6.0 (renamed: CTFontManagerRegisterFontURLs(_:_:_:_:))

## Declaration

```swift
func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool
```

```c
extern bool CTFontManagerRegisterFontsForURLs(CFArrayRef fontURLs, CTFontManagerScope scope, CFArrayRef*errors);
```

## Return Value

Returns `true` if registration of all font URLs was successful, otherwise `false`.

## Parameters

- `fontURLs`: Array of font URLs.
- `scope`: Scope constant defining the availability and lifetime of the registration. See [`CTFontManagerScope`](./ctfontmanagerscope.md) for values to pass for this parameter.
- `errors`: Pointer to an array of CFError objects which, in case of failed registration, contain error information. Each error contains a CFArray of font URLs corresponding to [`kCTFontManagerErrorFontURLsKey`](./kctfontmanagererrorfonturlskey.md). These URLs represent the font files that caused the error and were not successfully registered. The array must be released by the caller. Can be `NULL`.

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
- [func CTFontManagerRegisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerregistergraphicsfont%28_,_%29.md)
  Registers the specified graphics font with the font manager.
- [func CTFontManagerSetAutoActivationSetting(CFString?, CTFontManagerAutoActivationSetting)](./ctfontmanagersetautoactivationsetting%28_,_%29.md)
  Sets the auto-activation setting for the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontsforurls(_:_:_:))*