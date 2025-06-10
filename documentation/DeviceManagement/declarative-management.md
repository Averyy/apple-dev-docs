# Declarative Management

**Framework**: Device Management  
**Kind**: httpRequest

Sends declarative management requests to the server.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Integrating Declarative Management](integrating-declarative-management.md)

#### Discussion

The `Data` field is optional, depending on the `Endpoint` value, as described below:

The endpoint value is a path with three segments separated by a slash character (`/`). The first segment is always `declaration`. The second segment indicates the declaration type and is one of `activation`, `asset`, `configuration`, or `management`. The third segment is the `Identifier` of the declaration to fetch.

A successful response to this request is a `200 OK` HTTP status, with a response body that’s a JSON object representing the requested declaration. If the declaration isn’t present on the server, it needs to return a `404 Not Found` HTTP status response to the device. That causes the device to remove any corresponding declaration that is present on it.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |

## Topics

### Requests
- [object DeclarativeManagementRequest](declarativemanagementrequest.md)
  The declarative management request details.

## Request Body

The request object the system sends for the `DeclarativeManagement` request.

## See Also

- [Get Server Supported Declarations](declaration-items.md)
  Get a list of the declarations available on the server.
- [Get the Device Status](status.md)
  The request for getting the status of a device.
- [Get the Device Token](tokens.md)
  The request for sending the device token details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarative-management)*