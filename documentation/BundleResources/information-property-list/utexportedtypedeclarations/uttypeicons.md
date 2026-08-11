# UTTypeIcons

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary that describes how the system represents this type as an icon or symbol.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+



**Type**: dictionary

#### Discussion

This dictionary can include information about document icons, along with other icon-related data. When you provide document icon information in this key, the system generates the document icon at runtime by layering the assets you specify onto the standard folded-corner document shape. You can supply any combination of a background fill, a center badge image, and a text label. The system scales, masks, and composites them automatically.

All sub-keys are optional. If you omit a sub-key, the system substitutes a default: the app’s icon for the badge, the file extension for the text label, and no custom fill for the background.

## Topics

### Document icon resources
- [UTTypeIconBackgroundName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbackgroundname.md)
  The name of an icon set in your app’s asset catalog to use as the background fill of the document icon.
- [UTTypeIconBadgeName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeiconbadgename.md)
  The name of an icon set in your app’s asset catalog to use as the center badge image of the document icon.
- [UTTypeIconText](information-property-list/utexportedtypedeclarations/uttypeicons/uttypeicontext.md)
  A short string the system renders at the bottom edge of the document icon.
### Symbol representation
- [UTTypeSymbolName](information-property-list/utexportedtypedeclarations/uttypeicons/uttypesymbolname.md)
  The name of an SF Symbol that represents this type.

## See Also

- [UTTypeConformsTo](information-property-list/utexportedtypedeclarations/uttypeconformsto.md)
  The Uniform Type Identifier types that this type conforms to.
- [UTTypeDescription](information-property-list/utexportedtypedeclarations/uttypedescription.md)
  A description for this type.
- [UTTypeIconFile](information-property-list/utexportedtypedeclarations/uttypeiconfile.md)
  The bundle icon resource to associate with this type.
- [UTTypeIconFiles](information-property-list/utexportedtypedeclarations/uttypeiconfiles.md)
  One or more bundle icon resources to associate with this type.
- [UTTypeIdentifier](information-property-list/utexportedtypedeclarations/uttypeidentifier.md)
  The Uniform Type Identifier to assign to this type.
- [UTTypeReferenceURL](information-property-list/utexportedtypedeclarations/uttypereferenceurl.md)
  The webpage for a reference document that describes this type.
- [UTTypeTagSpecification](information-property-list/utexportedtypedeclarations/uttypetagspecification.md)
  A dictionary defining one or more equivalent type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/utexportedtypedeclarations/uttypeicons)*