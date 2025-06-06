# DHCPInfoGetOptionData

**Framework**: System Configuration  
**Kind**: func

Returns DHCP option data, if present.

**Availability**:
- macOS 10.1+

## Declaration

```swift
CFDataRef DHCPInfoGetOptionData(CFDictionaryRef info, UInt8 code);
```

#### Return Value

The DHCP option data if present, or `NULL` if the data is not present. You must not release the return value.

## Parameters

- `info`: The DHCP information dictionary returned by  . Do not pass in a   dictionary.
- `code`: The DHCP option code to get data for. (See RFC 2132 for more information on this code.)

## See Also

- [SCDynamicStoreCopyDHCPInfo](scdynamicstorecopydhcpinfo.md)
  Returns the DHCP information for the specified service.
- [DHCPInfoGetLeaseStartTime](dhcpinfogetleasestarttime.md)
  Returns the lease start time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpinfogetoptiondata)*