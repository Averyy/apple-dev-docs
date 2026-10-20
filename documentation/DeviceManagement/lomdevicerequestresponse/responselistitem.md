# LOMDeviceRequestResponse.ResponseListItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes a response list item.

**Availability**:
- macOS 11.0+

## Declaration

```
object LOMDeviceRequestResponse.ResponseListItem
```

## Properties

- `DeviceRequestReturnError` (string): If present, a description of the error for a failed request.
- `DeviceRequestSuccess` (boolean) *(required)*: If `true`, the request was successful.
- `DeviceRequestUUID` (string) *(required)*: The unique identifier of the request for this response list item.

## See Also

### Objects
- [object LOMDeviceRequestResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lomdevicerequestresponse/responselistitem)*