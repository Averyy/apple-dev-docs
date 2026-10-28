# CNMarkPortalOffline

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Informs Captive Network Support that the device is not authenticated on a captive network.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```c
Boolean CNMarkPortalOffline(CFStringRef interfaceName);
```

## Return Value

`TRUE` if the operation succeeded; otherwise, `FALSE`.

## Parameters

- `interfaceName`: The name of the interface that is now offline.

## See Also

### Functions
- [CNCopySupportedInterfaces](./cncopysupportedinterfaces.md)
  Returns the names of all network interfaces Captive Network Support is monitoring.
- [CNMarkPortalOnline](./cnmarkportalonline.md)
  Informs Captive Network Support that the application has successfully authenticated the device to a captive network. Captive Network Support notifies the rest of the system that WiFi is a viable interface.
- [CNSetSupportedSSIDs](./cnsetsupportedssids.md)
  Specifies an updated list of captive network SSIDs that the application performs authentication on.
- [DHCPInfoGetLeaseExpirationTime](./dhcpinfogetleaseexpirationtime.md)
  Returns the lease expiration time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/cnmarkportaloffline)*