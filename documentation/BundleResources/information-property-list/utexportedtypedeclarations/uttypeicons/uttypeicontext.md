# UTTypeIconText

**Framework**: Bundle Resources  
**Kind**: typealias

A short string the system renders at the bottom edge of the document icon.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+



**Type**: string

#### Discussion

This key is optional. If you omit this key, the system displays the file extension at the bottom of the document icon.

If you set this key, the system displays the string you provide instead of the file extension — for example, `scene` instead of `scn`. The system automatically scales the text to fit and capitalizes every letter. Keep the string short enough to remain legible at the smallest icon sizes.

## See Also

- [UTTypeIconBackgroundName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbackgroundname.md)
  The name of an icon set in your app’s asset catalog to use as the background fill of the document icon.
- [UTTypeIconBadgeName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbadgename.md)
  The name of an icon set in your app’s asset catalog to use as the center badge image of the document icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/utexportedtypedeclarations/uttypeicons/uttypeicontext)*