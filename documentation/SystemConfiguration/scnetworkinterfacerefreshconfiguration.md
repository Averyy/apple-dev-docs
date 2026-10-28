# SCNetworkInterfaceRefreshConfiguration

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Sends a notification to interested configuration agents to have them immediately retry their configuration over a particular network interface.

**Availability**:
- macOS 10.1+ - Deprecated in 10.5

> **Deprecated**: Use the [`SCNetworkInterfaceForceConfigurationRefresh(_:)`](./scnetworkinterfaceforceconfigurationrefresh%28_%29.md) function instead.

## Declaration

```c
Boolean SCNetworkInterfaceRefreshConfiguration(CFStringRef ifName);
```

## Return Value

`TRUE` if the notification was sent; otherwise, `FALSE`.

## Discussion

This function must be invoked by root (in other words, the user with uid equal to `0`).

## Parameters

- `ifName`: The BSD name of the network interface, such as `CFSTR("en0")`.

## See Also

### Group
- [SCNetworkCheckReachabilityByAddress](./scnetworkcheckreachabilitybyaddress.md)
  Determines whether the specified network address is reachable using the current network configuration.
- [SCNetworkCheckReachabilityByName](./scnetworkcheckreachabilitybyname.md)
  Determines whether the specified network host or node name is reachable using the current network configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkinterfacerefreshconfiguration)*