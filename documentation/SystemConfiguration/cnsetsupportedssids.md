# CNSetSupportedSSIDs

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Specifies an updated list of captive network SSIDs that the application performs authentication on.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```c
Boolean CNSetSupportedSSIDs(CFArrayRef ssidArray);
```

#### Return Value

`TRUE` if the list is successfully updated; otherwise, `FALSE`.

#### Discussion

The list is maintained for as long as the application is installed.

Providing a new list replaces any earlier list the application has provided.

## Parameters

- `ssidArray`: An array of `CFString` objects representing the SSIDs the application supports.

## See Also

### Functions
- [CNCopySupportedInterfaces](./cncopysupportedinterfaces.md)
  Returns the names of all network interfaces Captive Network Support is monitoring.
- [CNMarkPortalOffline](./cnmarkportaloffline.md)
  Informs Captive Network Support that the device is not authenticated on a captive network.
- [CNMarkPortalOnline](./cnmarkportalonline.md)
  Informs Captive Network Support that the application has successfully authenticated the device to a captive network. Captive Network Support notifies the rest of the system that WiFi is a viable interface.
- [DHCPInfoGetLeaseExpirationTime](./dhcpinfogetleaseexpirationtime.md)
  Returns the lease expiration time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/cnsetsupportedssids)*