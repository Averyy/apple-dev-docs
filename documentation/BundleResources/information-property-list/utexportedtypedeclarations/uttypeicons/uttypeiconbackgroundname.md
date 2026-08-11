# UTTypeIconBackgroundName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of an icon set in your app’s asset catalog to use as the background fill of the document icon.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+



**Type**: string

#### Discussion

This key is optional. If you omit this key, the system produces the document icon with no custom background fill.

If you set this key, the system scales the icon set to fit the document icon canvas and masks it to the folded-corner document shape before compositing. Avoid placing important content in the top-right corner of the image because the system draws the folded corner on top of that area.

## See Also

- [UTTypeIconBadgeName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbadgename.md)
  The name of an icon set in your app’s asset catalog to use as the center badge image of the document icon.
- [UTTypeIconText](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeicontext.md)
  A short string the system renders at the bottom edge of the document icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbackgroundname)*