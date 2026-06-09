# AccessibilityDeclarationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of accessibility declarations.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object AccessibilityDeclarationsResponse
```

## Properties

- `data` ([AccessibilityDeclaration]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AccessibilityDeclaration](accessibilitydeclaration.md)
  An app’s self-reported accessibility features and conformance information submitted for App Store review.
- [object AccessibilityDeclarationCreateRequest](accessibilitydeclarationcreaterequest.md)
  The request body you use to create an accessibility declaration for an app.
- [object AccessibilityDeclarationResponse](accessibilitydeclarationresponse.md)
  A response containing a single accessibility declaration for an app.
- [object AccessibilityDeclarationUpdateRequest](accessibilitydeclarationupdaterequest.md)
  The request body you use to update an accessibility declaration for an app.
- [object AppAccessibilityDeclarationsLinkagesResponse](appaccessibilitydeclarationslinkagesresponse.md)
- [type DeviceFamily](devicefamily.md)
  String that represents a device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/accessibilitydeclarationsresponse)*