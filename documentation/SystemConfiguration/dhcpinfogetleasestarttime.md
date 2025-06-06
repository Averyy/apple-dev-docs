# DHCPInfoGetLeaseStartTime

**Framework**: System Configuration  
**Kind**: func

Returns the lease start time data.

**Availability**:
- macOS 10.1+

## Declaration

```swift
CFDateRef DHCPInfoGetLeaseStartTime(CFDictionaryRef info);
```

#### Return Value

Data that corresponds to the lease start time, if this information is present, or `NULL` if the information is not present or if the configuration method is not DHCP.

## Parameters

- `info`: The DHCP information dictionary returned by  . Do not pass in a   dictionary.

## See Also

- [SCDynamicStoreCopyDHCPInfo](scdynamicstorecopydhcpinfo.md)
  Returns the DHCP information for the specified service.
- [DHCPInfoGetOptionData](dhcpinfogetoptiondata.md)
  Returns DHCP option data, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpinfogetleasestarttime)*