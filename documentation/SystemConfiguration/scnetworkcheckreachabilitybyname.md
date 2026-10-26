# SCNetworkCheckReachabilityByName

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Determines whether the specified network host or node name is reachable using the current network configuration.

**Availability**:
- macOS 10.1+ - Deprecated in 10.6

> **Deprecated**: See the discussion for a coding alternative.

## Declaration

```c
Boolean SCNetworkCheckReachabilityByName(const char *nodename, SCNetworkConnectionFlags *flags);
```

#### Return Value

`TRUE` if the network connection flags are valid; `FALSE` if the status could not be determined.

#### Discussion

This function is deprecated, but you can get equivalent results using the following code:

```objc
SCNetworkReachabilityRef target;
SCNetworkConnectionFlags flags = 0;
Boolean ok;
target = SCNetworkReachabilityCreateWithName(NULL, name);
ok = SCNetworkReachabilityGetFlags(target, &flags);
CFRelease(target);
```

## Parameters

- `nodename`: The node name of the desired host. This is the same name that would be passed to the gethostbyname(3) or getaddrinfo(3) functions.
- `flags`: A pointer to memory that, on output, will be filled with a set of [`SCNetworkConnectionFlags`](./scnetworkconnectionflags.md) values detailing the reachability of the specified address

## See Also

### Group
- [SCNetworkCheckReachabilityByAddress](./scnetworkcheckreachabilitybyaddress.md)
  Determines whether the specified network address is reachable using the current network configuration.
- [SCNetworkInterfaceRefreshConfiguration](./scnetworkinterfacerefreshconfiguration.md)
  Sends a notification to interested configuration agents to have them immediately retry their configuration over a particular network interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkcheckreachabilitybyname)*