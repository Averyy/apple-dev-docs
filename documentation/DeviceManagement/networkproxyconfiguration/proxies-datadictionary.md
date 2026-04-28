# NetworkProxyConfiguration.Proxies

**Framework**: Device Management  
**Kind**: dictionary

The payload for configuring network proxies.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object NetworkProxyConfiguration.Proxies
```

## Properties

- `ExceptionsList` ([string]): The list of hosts and domains that should bypass proxy settings.
- `FallBackAllowed` (integer): If `1`, enables fallback. Default is `1`. For managed devices, if not supplied, the default is `0`.
- `FTPEnable` (integer): If `true`, enables FTP proxy.
- `FTPPassive` (integer): If `true`, enables passive FTP mode.
- `FTPPort` (integer): The FTP proxy port.
- `FTPProxy` (string): The host name or IP address for the FTP proxy.
- `GopherEnable` (integer): If `true`, enables gopher proxy.
- `GopherPort` (integer): The gopher proxy port.
- `GopherProxy` (string): The host name or IP address for the gopher proxy.
- `HTTPEnable` (integer): If `true`, enables web proxy.
- `HTTPPort` (integer): The web proxy port.
- `HTTPProxy` (string): The host name or IP address for the web proxy.
- `HTTPSEnable` (integer): If `true`, enables secure web proxy.
- `HTTPSPort` (integer): The secure web proxy port.
- `HTTPSProxy` (string): The host name or IP address for the secure web proxy.
- `ProxyAutoConfigEnable` (integer): If `true`, enables automatic proxy configuration.
- `ProxyAutoConfigURLString` (string): The automatic proxy configuration URL.
- `ProxyCaptiveLoginAllowed` (integer): If 1, allows client to log into captive portal network.
- `RTSPEnable` (integer): If `true`, enable streaming proxy.
- `RTSPPort` (integer): The streaming proxy port.
- `RTSPProxy` (string): The host name or IP address for the streaming proxy.
- `SOCKSEnable` (integer): If `true`, enable the SOCKS proxy.
- `SOCKSPortinteger` (integer): The SOCKS proxy port.
- `SOCKSProxy` (string): The host name or IP address for the SOCKS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkproxyconfiguration/proxies-data.dictionary)*