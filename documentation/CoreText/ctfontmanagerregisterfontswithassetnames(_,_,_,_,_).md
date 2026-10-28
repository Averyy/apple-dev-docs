# CTFontManagerRegisterFontsWithAssetNames(_:_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Registers named font assets in the specified bundle with the font manager.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func CTFontManagerRegisterFontsWithAssetNames(_ fontAssetNames: CFArray, _ bundle: CFBundle?, _ scope: CTFontManagerScope, _ enabled: Bool, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

```c
extern void CTFontManagerRegisterFontsWithAssetNames(CFArrayRef fontAssetNames, CFBundleRef bundle, CTFontManagerScope scope, bool enabled, bool (^registrationHandler)(CFArrayRef errors, bool done));
```

## Discussion

Registered fonts are discoverable through font descriptor matching in the calling process.

Calling this function extracts the font assets from the asset catalog and registers them. You must make this call after the completion handler of either [`beginAccessingResources(completionHandler:)`](../Foundation/nsbundleresourcerequest/beginaccessingresources%28completionhandler%29.md): or [`conditionallyBeginAccessingResources(completionHandler:)`](../Foundation/nsbundleresourcerequest/conditionallybeginaccessingresources%28completionhandler%29.md) is called successfully.

Name the assets using PostScript names for individual faces, or family names for variable or collection fonts. You can use the same names to unregister the fonts with [`CTFontManagerUnregisterFontDescriptors(_:_:_:)`](./ctfontmanagerunregisterfontdescriptors%28_,_,_%29.md).

## Parameters

- `fontAssetNames`: An array of font name assets in the asset catalog.
- `bundle`: A bundle that contains the asset catalog. Passing `NULL` resolves to the main bundle.
- `scope`: A scope constant that defines the availability and lifetime of the registration. On iOS, the only supported scope is [`CTFontManagerScope.persistent`](./ctfontmanagerscope/persistent.md), which means the fonts aren’t automatically available to other processes. Other processes can call [`CTFontManagerRequestFonts(_:_:)`](./ctfontmanagerrequestfonts%28_,_%29.md) to get access to the fonts. See [`CTFontManagerScope`](./ctfontmanagerscope.md) for more details.
- `enabled`: A Boolean value that indicates whether the font assets should be enabled for font descriptor matching and discoverable through [`CTFontManagerRequestFonts(_:_:)`](./ctfontmanagerrequestfonts%28_,_%29.md).
- `registrationHandler`: A block called as errors arise or upon completion.

  The block’s `errors` parameter contains an array of [`CFError`](../CoreFoundation/cferror.md) references; an empty array indicates no errors. Each error reference contains a [`CFArray`](../CoreFoundation/cfarray.md) of font asset names corresponding to [`kCTFontManagerErrorFontAssetNameKey`](./kctfontmanagererrorfontassetnamekey.md). These represent the font asset names causing the error and failing to register successfully.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontswithassetnames(_:_:_:_:_:))*