# MdmServerStatus

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent the operational status of a device management service.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
string MdmServerStatus
```

## Possible Values

- `ACTIVE`
- `DELETED`
- `INACTIVE`

## Discussion

- Possible Values

  - ACTIVE: The server is active and able to manage devices.
  - INACTIVE: The server is currently inactive.
  - DELETED: The server has been removed from the organization.

## See Also

### Related Types
- [type MdmServerProductFamily](./mdmserverproductfamily.md)
  Strings that represent a product family that can be assigned as a default to a device management service.
- [object MdmServerCertificate](./mdmservercertificate.md)
  The X.509 certificate to associate with a device management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmserverstatus)*