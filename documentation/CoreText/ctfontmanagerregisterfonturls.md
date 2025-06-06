# CTFontManagerRegisterFontURLs(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func

Registers fonts from the specified font URLs with the font manager.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CTFontManagerRegisterFontURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ enabled: Bool, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

#### Discussion

Registered fonts are discoverable through font descriptor matching in the calling process.

## Parameters

- `fontURLs`: A file URL for the fonts or collections (in TTC or OTC format) to register. After registering fonts from a file, don’t move or rename the file.
- `scope`: A scope constant that defines the availability and lifetime of the registration. If you specify   when you register fonts on iOS, those fonts aren’t automatically available to other processes. Other processes can call   to get access to those fonts. See   for more details.
- `enabled`: A Boolean value that indicates whether the font derived from the URL should be enabled for font descriptor matching and discoverable through  .
- `registrationHandler`: This block may be called multiple times during the registration process. The   parameter becomes   when the registration process completes. Return   from the block to stop the registration operation, like after receiving an error.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfonturls(_:_:_:_:))*