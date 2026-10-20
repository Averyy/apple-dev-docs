# CTFontManagerRegisterFontDescriptors(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Registers font descriptors with the font manager.

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
func CTFontManagerRegisterFontDescriptors(_ fontDescriptors: CFArray, _ scope: CTFontManagerScope, _ enabled: Bool, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

```c
extern void CTFontManagerRegisterFontDescriptors(CFArrayRef fontDescriptors, CTFontManagerScope scope, bool enabled, bool (^registrationHandler)(CFArrayRef errors, bool done));
```

#### Discussion

Registered fonts are discoverable through font descriptor matching in the calling process.

Fonts descriptors registered in a disabled state (the `enabled` parameter set to [`false`](../Swift/false.md)) aren’t immediately available for descriptor matching, but the font manager knows the descriptors can be made available if necessary. You can enable these descriptors by calling this function again with the `enabled` parameter set to [`true`](../Swift/true.md). This operation may fail if there’s another registered and enabled font with the same PostScript name.

## Parameters

- `fontDescriptors`: An array of font descriptors to register. The font descriptor keys for registration are [`kCTFontURLAttribute`](./kctfonturlattribute.md), [`kCTFontNameAttribute`](./kctfontnameattribute.md), [`kCTFontFamilyNameAttribute`](./kctfontfamilynameattribute.md), or [`kCTFontRegistrationUserInfoAttribute`](./kctfontregistrationuserinfoattribute.md).
- `scope`: A scope constant that defines the availability and lifetime of the registration. If you specify [`CTFontManagerScope.persistent`](./ctfontmanagerscope/persistent.md) when you register fonts on iOS, those fonts aren’t automatically available to other processes. Other processes can call [`CTFontManagerRequestFonts(_:_:)`](./ctfontmanagerrequestfonts%28_,_%29.md) to get access to those fonts. See [`CTFontManagerScope`](./ctfontmanagerscope.md) for more details.
- `enabled`: A Boolean value that indicates whether the font descriptors should be enabled for font descriptor matching and discoverable though [`CTFontManagerRequestFonts(_:_:)`](./ctfontmanagerrequestfonts%28_,_%29.md).
- `registrationHandler`: A block called as errors arise or upon completion.

  The block’s `errors` parameter contains an array of [`CFError`](../CoreFoundation/cferror.md) references; an empty array indicates no errors. Each error reference contains a [`CFArray`](../CoreFoundation/cfarray.md) of font descriptors corresponding to [`kCTFontManagerErrorFontDescriptorsKey`](./kctfontmanagererrorfontdescriptorskey.md). These represent the font descriptors causing the error and failing to register successfully.

  This block may be called multiple times during the registration process. The `done` parameter becomes [`true`](../Swift/true.md) when the registration process completes. Return [`false`](../Swift/false.md) from the block to stop the registration operation, like after receiving an error.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontdescriptors(_:_:_:_:))*