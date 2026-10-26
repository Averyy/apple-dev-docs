# DHCPInfoGetLeaseExpirationTime

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the lease expiration time data.

**Availability**:
- macOS 10.8+

## Declaration

```c
CFDateRefDHCPInfoGetLeaseExpirationTime(CFDictionaryRef info);
```

## See Also

### Functions
- [CNCopySupportedInterfaces](./cncopysupportedinterfaces.md)
  Returns the names of all network interfaces Captive Network Support is monitoring.
- [CNMarkPortalOffline](./cnmarkportaloffline.md)
  Informs Captive Network Support that the device is not authenticated on a captive network.
- [CNMarkPortalOnline](./cnmarkportalonline.md)
  Informs Captive Network Support that the application has successfully authenticated the device to a captive network. Captive Network Support notifies the rest of the system that WiFi is a viable interface.
- [CNSetSupportedSSIDs](./cnsetsupportedssids.md)
  Specifies an updated list of captive network SSIDs that the application performs authentication on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpinfogetleaseexpirationtime)*