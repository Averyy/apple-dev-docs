# DHCPInfoGetLeaseStartTime

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the lease start time data.

**Availability**:
- macOS 10.1+

## Declaration

```c
CFDateRefDHCPInfoGetLeaseStartTime(CFDictionaryRef info);
```

#### Return Value

Data that corresponds to the lease start time, if this information is present, or `NULL` if the information is not present or if the configuration method is not DHCP.

## Parameters

- `info`: The DHCP information dictionary returned by [`SCDynamicStoreCopyDHCPInfo`](./scdynamicstorecopydhcpinfo.md). Do not pass in a `NULL` dictionary.

## See Also

### Group
- [SCDynamicStoreCopyDHCPInfo](./scdynamicstorecopydhcpinfo.md)
  Returns the DHCP information for the specified service.
- [DHCPInfoGetOptionData](./dhcpinfogetoptiondata.md)
  Returns DHCP option data, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpinfogetleasestarttime)*