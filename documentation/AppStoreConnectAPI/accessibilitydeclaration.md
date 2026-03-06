# AccessibilityDeclaration

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents an accessibility declarations resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object AccessibilityDeclaration
```

## Topics

### Dictionaries
- [object AccessibilityDeclaration.Attributes](accessibilitydeclaration/attributes-data.dictionary.md)
  The attributes you set that describe the accessibility declaration resource.

## Properties

- `attributes` (AccessibilityDeclaration.Attributes): Attributes that describe this accessibility declaration resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `links` (ResourceLinks): Navigational links that include the self-link.
- `type` (string) *(required)*: The resource type.

## See Also

- [object AccessibilityDeclarationsResponse](accessibilitydeclarationsresponse.md)
  A response that contains a list of accessibility declaration resources.
- [object AccessibilityDeclarationCreateRequest](accessibilitydeclarationcreaterequest.md)
  The request body you use to create an accessibility declaration for an app.
- [object AccessibilityDeclarationResponse](accessibilitydeclarationresponse.md)
  A response that contains a single accessibility declaration resource.
- [object AccessibilityDeclarationUpdateRequest](accessibilitydeclarationupdaterequest.md)
  The request body you use to update an accessibility declaration for an app.
- [object AppAccessibilityDeclarationsLinkagesResponse](appaccessibilitydeclarationslinkagesresponse.md)
- [type DeviceFamily](devicefamily.md)
  String that represents a device family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/accessibilitydeclaration)*