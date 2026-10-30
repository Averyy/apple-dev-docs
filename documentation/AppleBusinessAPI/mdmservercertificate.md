# MdmServerCertificate

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The X.509 certificate to associate with a device management service.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object MdmServerCertificate
```

## Properties

- `name` (string) *(required)*: The certificate’s file name.
- `data` (byte) *(required)*: The Base64-encoded certificate data.

## See Also

### Related Types
- [type MdmServerStatus](./mdmserverstatus.md)
  Strings that represent the operational status of a device management service.
- [type MdmServerProductFamily](./mdmserverproductfamily.md)
  Strings that represent a product family that can be assigned as a default to a device management service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmservercertificate)*