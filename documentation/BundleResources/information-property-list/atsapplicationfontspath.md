# ATSApplicationFontsPath

**Framework**: Bundle Resources  
**Kind**: typealias

The location of a font file or folder of fonts in the bundle’s Resources folder.

**Availability**:
- macOS 10.0+

#### Discussion

If you set this key, the system allows the app in the bundle to use the fonts at the specified path. Set this key to the path relative to the bundle’s `Resources` folder. For example, if the fonts are in `.../Resources/MyFonts`, set this key to `MyFonts/`.

## See Also

- [UIAppFonts](information-property-list/uiappfonts.md)
  App-specific font files located in the bundle and that the system loads at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/atsapplicationfontspath)*