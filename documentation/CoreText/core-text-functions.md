# Core Text Functions

**Framework**: Core Text  
**Role**: API Collection

## Topics

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
- [func CTFontManagerSetAutoActivationSetting(CFString?, CTFontManagerAutoActivationSetting)](./ctfontmanagersetautoactivationsetting%28_,_%29.md)
  Sets the auto-activation setting for the specified bundle identifier.
- [func CTFontManagerUnregisterFontsForURL(CFURL, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerunregisterfontsforurl%28_,_,_%29.md)
  Unregisters fonts from the specified font URL with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching.
- [func CTFontManagerUnregisterFontsForURLs(CFArray, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](./ctfontmanagerunregisterfontsforurls%28_,_,_%29.md)
  Unregisters fonts from the specified array of font URLs with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching.
- [func CTFontManagerUnregisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./ctfontmanagerunregistergraphicsfont%28_,_%29.md)
  Unregisters the specified graphics font with the font manager.
- [func CTFontManagerCopyRegisteredFontDescriptors(CTFontManagerScope, Bool) -> CFArray](./ctfontmanagercopyregisteredfontdescriptors%28_,_%29.md)
  Retrieves the font descriptors that were registered with the font manager.
- [func CTFontManagerCreateFontDescriptorsFromData(CFData) -> CFArray](./ctfontmanagercreatefontdescriptorsfromdata%28_%29.md)
  Creates an array of font descriptors for the fonts in the supplied data.
- [func CTFontManagerRegisterFontDescriptors(CFArray, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](./ctfontmanagerregisterfontdescriptors%28_,_,_,_%29.md)
  Registers font descriptors with the font manager.
- [func CTFontManagerRegisterFontURLs(CFArray, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](./ctfontmanagerregisterfonturls%28_,_,_,_%29.md)
  Registers fonts from the specified font URLs with the font manager.
- [func CTFontManagerRegisterFontsWithAssetNames(CFArray, CFBundle?, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](./ctfontmanagerregisterfontswithassetnames%28_,_,_,_,_%29.md)
  Registers named font assets in the specified bundle with the font manager.
- [func CTFontManagerRequestFonts(CFArray, (CFArray) -> Void)](./ctfontmanagerrequestfonts%28_,_%29.md)
  Resolves font descriptors specified on input.
- [func CTFontManagerUnregisterFontDescriptors(CFArray, CTFontManagerScope, ((CFArray, Bool) -> Bool)?)](./ctfontmanagerunregisterfontdescriptors%28_,_,_%29.md)
  Unregisters font descriptors with the font manager.
- [func CTFontManagerUnregisterFontURLs(CFArray, CTFontManagerScope, ((CFArray, Bool) -> Bool)?)](./ctfontmanagerunregisterfonturls%28_,_,_%29.md)
  Unregisters fonts from the specified font URLs with the font manager.
- [func CTGetCoreTextVersion() -> UInt32](./ctgetcoretextversion%28%29.md)
  Returns the version of the Core Text framework.
- [func CTRubyAnnotationCreate(CTRubyAlignment, CTRubyOverhang, CGFloat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation](./ctrubyannotationcreate%28_,_,_,_%29.md)
  Creates an immutable ruby annotation object.
- [func CTRubyAnnotationCreateCopy(CTRubyAnnotation) -> CTRubyAnnotation](./ctrubyannotationcreatecopy%28_%29.md)
  Creates an immutable copy of a ruby annotation object.
- [func CTRubyAnnotationCreateWithAttributes(CTRubyAlignment, CTRubyOverhang, CTRubyPosition, CFString, CFDictionary) -> CTRubyAnnotation](./ctrubyannotationcreatewithattributes%28_,_,_,_,_%29.md)
  Creates an immutable ruby annotation object with the specified attributes.
- [func CTRubyAnnotationGetAlignment(CTRubyAnnotation) -> CTRubyAlignment](./ctrubyannotationgetalignment%28_%29.md)
  Retrieves the alignment value of a ruby annotation object.
- [func CTRubyAnnotationGetOverhang(CTRubyAnnotation) -> CTRubyOverhang](./ctrubyannotationgetoverhang%28_%29.md)
  Retrieves the overhang value of a ruby annotation object.
- [func CTRubyAnnotationGetSizeFactor(CTRubyAnnotation) -> CGFloat](./ctrubyannotationgetsizefactor%28_%29.md)
  Retrieves the size factor of a ruby annotation object.
- [func CTRubyAnnotationGetTextForPosition(CTRubyAnnotation, CTRubyPosition) -> CFString?](./ctrubyannotationgettextforposition%28_,_%29.md)
  Retrieves the ruby text for a particular position in a ruby annotation.
- [func CTRubyAnnotationGetTypeID() -> CFTypeID](./ctrubyannotationgettypeid%28%29.md)
  Retrieves the type of the ruby annotation object.
- [func CTFontCopyNameForGlyph(CTFont, CGGlyph) -> CFString?](./ctfontcopynameforglyph%28_,_%29.md)
  Retrieves the name for the specified glyph.
- [func CTFontDrawImageFromAdaptiveImageProviderAtPoint(CTFont, any CTAdaptiveImageProviding, CGPoint, CGContext)](./ctfontdrawimagefromadaptiveimageprovideratpoint%28_,_,_,_%29.md)
- [func CTFontGetTypographicBoundsForAdaptiveImageProvider(CTFont, (any CTAdaptiveImageProviding)?) -> CGRect](./ctfontgettypographicboundsforadaptiveimageprovider%28_,_%29.md)
- [func CTFontHasTable(CTFont, CTFontTableTag) -> Bool](./ctfonthastable%28_,_%29.md)

## See Also

### Reference
- [Styling Attributed Strings](./styling-attributed-strings.md)
  Attributes to which Core Text responds when placed in a `CFAttributedString` object.
- [Core Text Structures](./core-text-structures.md)
- [Core Text Enumerations](./core-text-enumerations.md)
- [Core Text Constants](./core-text-constants.md)
- [Core Text Data Types](./core-text-data-types.md)
- [SFNT Support](./sfnt-support.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/core-text-functions)*