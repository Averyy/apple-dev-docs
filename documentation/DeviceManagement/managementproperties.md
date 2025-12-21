# ManagementProperties

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the properties on the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagementProperties
```

#### Discussion

Specify `com.apple.management.properties` as the declaration type.

##### Management Declaration Example

```json
{
    "Type": "com.apple.management.properties",
    "Identifier": "187C9F47-297C-4811-80C4-2E19D3C11963",
    "ServerToken": "526CE2FB-DB79-409A-825D-8C5DC5EE873E",
    "Payload": {
        "is-part-time": false,
        "groups": [
            "teacher",
            "grade 1",
            "grade 2",
            "it-admin"
        ]
    }
}
```

## See Also

- [object ManagementOrganizationInformation](managementorganizationinformation.md)
  The declaration to configure the managing organization’s contact information.
- [object ManagementServerCapabilities](managementservercapabilities.md)
  The declaration to configure the server’s feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managementproperties)*