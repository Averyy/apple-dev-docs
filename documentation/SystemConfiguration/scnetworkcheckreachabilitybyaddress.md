# SCNetworkCheckReachabilityByAddress

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Determines whether the specified network address is reachable using the current network configuration.

**Availability**:
- macOS 10.1+ - Deprecated in 10.6

> **Deprecated**: See the discussion for a coding alternative.

## Declaration

```c
Boolean SCNetworkCheckReachabilityByAddress(const struct sockaddr *address, socklen_t addrlen, SCNetworkConnectionFlags *flags);
```

#### Return Value

`TRUE` if the network connection flags are valid; `FALSE` if the status could not be determined.

#### Discussion

This function is deprecated, but you can get equivalent results using the following code:

```objc
SCNetworkReachabilityRef target;
SCNetworkConnectionFlags flags = 0;
Boolean ok;
target = SCNetworkReachabilityCreateWithAddress(NULL, address);
ok = SCNetworkReachabilityGetFlags(target, &flags);
CFRelease(target);
```

## Parameters

- `address`: The network address of the desired host.
- `addrlen`: The length, in bytes, of the address.
- `flags`: A pointer to memory that, on output, will be filled with a set of [`SCNetworkConnectionFlags`](./scnetworkconnectionflags.md) values detailing the reachability of the specified address

## See Also

### Group
- [SCNetworkCheckReachabilityByName](./scnetworkcheckreachabilitybyname.md)
  Determines whether the specified network host or node name is reachable using the current network configuration.
- [SCNetworkInterfaceRefreshConfiguration](./scnetworkinterfacerefreshconfiguration.md)
  Sends a notification to interested configuration agents to have them immediately retry their configuration over a particular network interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkcheckreachabilitybyaddress)*