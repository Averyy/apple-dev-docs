# UTTypeIconBadgeName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of an iconset in your app’s asset catalog to use as the center badge image of the document icon.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+



**Type**: string

#### Discussion

This key is optional. If you omit this key, the system automatically uses the app’s icon as the center badge.

If you set this key, the system uses the named iconset instead, positioning it at the center of the document icon canvas, then masks and scales it as needed.

## See Also

- [UTTypeIconBackgroundName](information-property-list/utimportedtypedeclarations/uttypeicons/uttypeiconbackgroundname.md)
  The name of an icon set in your app’s asset catalog to use as the background fill of the document icon.
- [UTTypeIconText](information-property-list/utimportedtypedeclarations/uttypeicons/uttypeicontext.md)
  A short string the system renders at the bottom edge of the document icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/utimportedtypedeclarations/uttypeicons/uttypeiconbadgename)*