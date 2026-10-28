# CTRubyAnnotationCreateWithAttributes(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates an immutable ruby annotation object with the specified attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func CTRubyAnnotationCreateWithAttributes(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ position: CTRubyPosition, _ string: CFString, _ attributes: CFDictionary) -> CTRubyAnnotation
```

```c
extern CTRubyAnnotationRefCTRubyAnnotationCreateWithAttributes(CTRubyAlignment alignment, CTRubyOverhang overhang, CTRubyPosition position, CFStringRef string, CFDictionaryRef attributes);
```

## Return Value

A reference to a [`CTRubyAnnotation`](./ctrubyannotation.md) object.

## Discussion

Use this function to create a ruby annotation object with more precise control of the annotation text.

## Parameters

- `alignment`: An alignment value that specifies how the ruby text and the base text align relative to each other.
- `overhang`: An overhang value that specifies how the ruby text overhangs adjacent characters.
- `position`: The position of the annotation text.
- `string`: An unformatted string whose attributes derive from the `attributes` parameter.
- `attributes`: An attribute dictionary to combine with `string`. If you don’t specify [`kCTFontAttributeName`](./kctfontattributename.md), the system deduces the ruby annotation’s font from the base text and uses a size factor of the [`CFNumber`](../CoreFoundation/cfnumber.md) value keyed by [`kCTRubyAnnotationSizeFactorAttributeName`](./kctrubyannotationsizefactorattributename.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyannotationcreatewithattributes(_:_:_:_:_:))*