# ManagementOrganizationInformation

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the managing organization’s contact information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagementOrganizationInformation
```

#### Discussion

Specify `com.apple.management.organization-info` as the declaration type.

##### Management Declaration Example

```json
{
    "Type": "com.apple.management.organization-info",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "Name": "Example, Inc.",
        "Email": "admin@example.com",
        "URL": "https://site.example.com/support"
    }
}
```

## Topics

### Objects
- [object ManagementOrganizationInformationProofObject](managementorganizationinformationproofobject.md)
  The additional properties that verify the identity and authenticity of the organization.

## See Also

- [object ManagementProperties](managementproperties.md)
  The declaration to configure the properties on the device.
- [object ManagementServerCapabilities](managementservercapabilities.md)
  The declaration to configure the server’s feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managementorganizationinformation)*