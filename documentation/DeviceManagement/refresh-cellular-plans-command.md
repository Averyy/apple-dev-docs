# Refresh Cellular Plans

**Framework**: Device Management  
**Kind**: httpRequest

Query a carrier URL for active eSIM cellular-plan profiles on a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

#### Discussion

This command is supported on iPad with iPadOS 13 and later and on iPhone with iOS 14 and later.

##### Error Codes

An error response uses one of the following error codes:

- `36001`: Unable to communicate with the cellular software stack.
- `36002`: The hardware doesn’t support this command.
- `36003`: The cellular stack was unable to perform the request. This error can also occur if the cellular stack is busy, in which case, retrying the command later may resolve the issue.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | NA |
| Required access right | NA |

##### Example Request and Response

## Topics

### Commands and responses
- [object RefreshCellularPlansCommand](refreshcellularplanscommand.md)
  The command to query a carrier URL for active eSIM cellular-plan profiles on a device.
- [object RefreshCellularPlansResponse](refreshcellularplansresponse.md)
  A response from the device after it processes the command to query a carrier URL for active eSIM cellular-plan profiles on a device.

## Request Body

The request object the server returns for the Refresh Cellular Plans Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/refresh-cellular-plans-command)*