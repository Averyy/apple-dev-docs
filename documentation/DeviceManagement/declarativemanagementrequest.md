# DeclarativeManagementRequest

**Framework**: Device Management  
**Kind**: dictionary

The declarative managmement request details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DeclarativeManagementRequest
```

#### Discussion

The `Data` field is optional, depending on the `Endpoint` value, as described below:

The endpoint value is a path with 3 segments separated by a / character. The first segment is always `declaration`. The second segment indicates the declaration type and is one of `activation`, `asset`, `configuration`, or `management`. The third segment is the `Identifier` of the declaration to fetch.

A successful response to this request is a `200 OK HTTP` status, with a response body that’s a JSON object representing the requested declaration. If the declaration isn’t present on the server, it must return a `404 Not Found HTTP` status response to the device. The device then considers that declaration to no longer exist on the server and removes any corresponding declaration present on the device.

## Topics

### Declaration Endpoints
- [declaration/activation/{identifier}](declaration-activation-_identifier_.md)
  The endpoint for fetching an activation declaration.
- [declaration/asset/{identifier}](declaration-asset-_identifier_.md)
  The endpoint for fetching an asset declaration.
- [declaration/configuration/{identifier}](declaration-configuration-_identifier_.md)
  The endpoint for fetching a configuration declaration.
- [declaration/management/{identifier}](declaration-management-_identifier_.md)
  The endpoint for fetching a management declaration.
### Declaration Response
- [object DeclarationResponse](declarationresponse.md)
  The details of a declaration, including its type and payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarativemanagementrequest)*