# Update the eSIM Cellular Plan

**Framework**: Device Management  
**Kind**: httpRequest

Query a carrier URL for active eSIM cellular-plan profiles on a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command is supported on iPad with iPadOS 13 and later and on iPhone with iOS 14 and later.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | - |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object RefreshCellularPlansCommand](refreshcellularplanscommand.md)
  The command to query a carrier URL for active eSIM cellular-plan profiles.
- [object RefreshCellularPlansResponse](refreshcellularplansresponse.md)
  A response from the device after it processes the command to query a carrier URL for active eSIM cellular-plan profiles.

## Request Body

The command to query a carrier URL for active eSIM cellular-plan profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/refresh-cellular-plans-command)*