# SCDynamicStoreCopyDHCPInfo

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the DHCP information for the specified service.

**Availability**:
- macOS 10.1+

## Declaration

```c
CFDictionaryRefSCDynamicStoreCopyDHCPInfo(SCDynamicStoreRef store, CFStringRef serviceID);
```

## Return Value

A dictionary containing DHCP information if successful, or `NULL` if unsuccessful. You must use the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release return values other than `NULL`.

## Discussion

Use [`DHCPInfoGetOptionData`](./dhcpinfogetoptiondata.md) to extract individual options from the dictionary returned by this function.

## Parameters

- `store`: The dynamic store session that should be used for communication with the server. If this is `NULL`, a temporary session is used.
- `serviceID`: The service ID. Pass `NULL` to retrieve information for the primary service.

## See Also

### Group
- [DHCPInfoGetOptionData](./dhcpinfogetoptiondata.md)
  Returns DHCP option data, if present.
- [DHCPInfoGetLeaseStartTime](./dhcpinfogetleasestarttime.md)
  Returns the lease start time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopydhcpinfo)*