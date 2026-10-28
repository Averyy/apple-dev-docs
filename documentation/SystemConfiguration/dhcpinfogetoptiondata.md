# DHCPInfoGetOptionData

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns DHCP option data, if present.

**Availability**:
- macOS 10.1+

## Declaration

```c
CFDataRefDHCPInfoGetOptionData(CFDictionaryRef info, UInt8 code);
```

## Return Value

The DHCP option data if present, or `NULL` if the data is not present. You must not release the return value.

## Parameters

- `info`: The DHCP information dictionary returned by [`SCDynamicStoreCopyDHCPInfo`](./scdynamicstorecopydhcpinfo.md). Do not pass in a `NULL` dictionary.
- `code`: The DHCP option code to get data for. (See RFC 2132 for more information on this code.)

## See Also

### Group
- [SCDynamicStoreCopyDHCPInfo](./scdynamicstorecopydhcpinfo.md)
  Returns the DHCP information for the specified service.
- [DHCPInfoGetLeaseStartTime](./dhcpinfogetleasestarttime.md)
  Returns the lease start time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpinfogetoptiondata)*