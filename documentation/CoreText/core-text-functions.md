# Core Text Functions

**Framework**: Core Text

## Topics

### Functions
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
- [func CTFontManagerSetAutoActivationSetting(CFString?, CTFontManagerAutoActivationSetting)](ctfontmanagersetautoactivationsetting(_:_:).md)
  Sets the auto-activation setting for the specified bundle identifier.
- [func CTFontManagerUnregisterFontsForURL(CFURL, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](ctfontmanagerunregisterfontsforurl(_:_:_:).md)
  Unregisters fonts from the specified font URL with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching.
- [func CTFontManagerUnregisterFontsForURLs(CFArray, CTFontManagerScope, UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool](ctfontmanagerunregisterfontsforurls(_:_:_:).md)
  Unregisters fonts from the specified array of font URLs with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching.
- [func CTFontManagerUnregisterGraphicsFont(CGFont, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](ctfontmanagerunregistergraphicsfont(_:_:).md)
  Unregisters the specified graphics font with the font manager.
- [func CTFontManagerCopyRegisteredFontDescriptors(CTFontManagerScope, Bool) -> CFArray](ctfontmanagercopyregisteredfontdescriptors(_:_:).md)
  Retrieves the font descriptors that were registered with the font manager.
- [func CTFontManagerCreateFontDescriptorsFromData(CFData) -> CFArray](ctfontmanagercreatefontdescriptorsfromdata(_:).md)
  Creates an array of font descriptors for the fonts in the supplied data.
- [func CTFontManagerRegisterFontDescriptors(CFArray, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](ctfontmanagerregisterfontdescriptors(_:_:_:_:).md)
  Registers font descriptors with the font manager.
- [func CTFontManagerRegisterFontURLs(CFArray, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](ctfontmanagerregisterfonturls(_:_:_:_:).md)
  Registers fonts from the specified font URLs with the font manager.
- [func CTFontManagerRegisterFontsWithAssetNames(CFArray, CFBundle?, CTFontManagerScope, Bool, ((CFArray, Bool) -> Bool)?)](ctfontmanagerregisterfontswithassetnames(_:_:_:_:_:).md)
  Registers named font assets in the specified bundle with the font manager.
- [func CTFontManagerRequestFonts(CFArray, (CFArray) -> Void)](ctfontmanagerrequestfonts(_:_:).md)
  Resolves font descriptors specified on input.
- [func CTFontManagerUnregisterFontDescriptors(CFArray, CTFontManagerScope, ((CFArray, Bool) -> Bool)?)](ctfontmanagerunregisterfontdescriptors(_:_:_:).md)
  Unregisters font descriptors with the font manager.
- [func CTFontManagerUnregisterFontURLs(CFArray, CTFontManagerScope, ((CFArray, Bool) -> Bool)?)](ctfontmanagerunregisterfonturls(_:_:_:).md)
  Unregisters fonts from the specified font URLs with the font manager.
- [func CTGetCoreTextVersion() -> UInt32](ctgetcoretextversion().md)
  Returns the version of the Core Text framework.
- [func CTRubyAnnotationCreate(CTRubyAlignment, CTRubyOverhang, CGFloat, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation](ctrubyannotationcreate(_:_:_:_:).md)
  Creates an immutable ruby annotation object.
- [func CTRubyAnnotationCreateCopy(CTRubyAnnotation) -> CTRubyAnnotation](ctrubyannotationcreatecopy(_:).md)
  Creates an immutable copy of a ruby annotation object.
- [func CTRubyAnnotationCreateWithAttributes(CTRubyAlignment, CTRubyOverhang, CTRubyPosition, CFString, CFDictionary) -> CTRubyAnnotation](ctrubyannotationcreatewithattributes(_:_:_:_:_:).md)
  Creates an immutable ruby annotation object with the specified attributes.
- [func CTRubyAnnotationGetAlignment(CTRubyAnnotation) -> CTRubyAlignment](ctrubyannotationgetalignment(_:).md)
  Retrieves the alignment value of a ruby annotation object.
- [func CTRubyAnnotationGetOverhang(CTRubyAnnotation) -> CTRubyOverhang](ctrubyannotationgetoverhang(_:).md)
  Retrieves the overhang value of a ruby annotation object.
- [func CTRubyAnnotationGetSizeFactor(CTRubyAnnotation) -> CGFloat](ctrubyannotationgetsizefactor(_:).md)
  Retrieves the size factor of a ruby annotation object.
- [func CTRubyAnnotationGetTextForPosition(CTRubyAnnotation, CTRubyPosition) -> CFString?](ctrubyannotationgettextforposition(_:_:).md)
  Retrieves the ruby text for a particular position in a ruby annotation.
- [func CTRubyAnnotationGetTypeID() -> CFTypeID](ctrubyannotationgettypeid().md)
  Retrieves the type of the ruby annotation object.
- [func CTFontCopyNameForGlyph(CTFont, CGGlyph) -> CFString?](ctfontcopynameforglyph(_:_:).md)
  Retrieves the name for the specified glyph.
- [func CTFontDrawImageFromAdaptiveImageProviderAtPoint(CTFont, any CTAdaptiveImageProviding, CGPoint, CGContext)](ctfontdrawimagefromadaptiveimageprovideratpoint(_:_:_:_:).md)
- [func CTFontGetTypographicBoundsForAdaptiveImageProvider(CTFont, (any CTAdaptiveImageProviding)?) -> CGRect](ctfontgettypographicboundsforadaptiveimageprovider(_:_:).md)
- [func CTFontHasTable(CTFont, CTFontTableTag) -> Bool](ctfonthastable(_:_:).md)

## See Also

- [Styling Attributed Strings](styling-attributed-strings.md)
  Attributes to which Core Text responds when placed in a `CFAttributedString` object.
- [Core Text Structures](core-text-structures.md)
- [Core Text Enumerations](core-text-enumerations.md)
- [Core Text Constants](core-text-constants.md)
- [Core Text Data Types](core-text-data-types.md)
- [SFNT Support](sfnt-support.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/core-text-functions)*