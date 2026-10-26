# CNCopySupportedInterfaces

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the names of all network interfaces Captive Network Support is monitoring.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```c
CFArrayRefCNCopySupportedInterfaces();
```

#### Return Value

The network interface names, as an array of [`CFString`](../CoreFoundation/cfstring.md) objects. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Functions
- [CNMarkPortalOffline](./cnmarkportaloffline.md)
  Informs Captive Network Support that the device is not authenticated on a captive network.
- [CNMarkPortalOnline](./cnmarkportalonline.md)
  Informs Captive Network Support that the application has successfully authenticated the device to a captive network. Captive Network Support notifies the rest of the system that WiFi is a viable interface.
- [CNSetSupportedSSIDs](./cnsetsupportedssids.md)
  Specifies an updated list of captive network SSIDs that the application performs authentication on.
- [DHCPInfoGetLeaseExpirationTime](./dhcpinfogetleaseexpirationtime.md)
  Returns the lease expiration time data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/cncopysupportedinterfaces)*