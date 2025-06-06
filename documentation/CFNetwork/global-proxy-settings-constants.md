# Global Proxy Settings Constants

**Framework**: CFNetwork

Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](cfnetworkcopysystemproxysettings().md).

## Topics

### Constants
- [let kCFNetworkProxiesExceptionsList: CFString](kcfnetworkproxiesexceptionslist.md)
  Value is a `CFArray` of `CFString` objects indicating host name patterns that should bypass the proxy.
- [let kCFNetworkProxiesExcludeSimpleHostnames: CFString](kcfnetworkproxiesexcludesimplehostnames.md)
  Value is a `CFNumber` object indicating whether simple host names are excluded. Simple host names are excluded if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesFTPEnable: CFString](kcfnetworkproxiesftpenable.md)
  Value is a `CFNumber` object indicating whether an FTP proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesFTPPassive: CFString](kcfnetworkproxiesftppassive.md)
  Value is a `CFNumber` object indicating whether an FTP proxy’s passive mode is enabled. The passive mode is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesFTPPort: CFString](kcfnetworkproxiesftpport.md)
  Value is a `CFNumber` object indicating the port number of an FTP proxy.
- [let kCFNetworkProxiesFTPProxy: CFString](kcfnetworkproxiesftpproxy.md)
  Value is a `CFString` object indicating the host name or IP number of an FTP proxy.
- [let kCFNetworkProxiesGopherEnable: CFString](kcfnetworkproxiesgopherenable.md)
  Value is a `CFNumber` object indicating whether a gopher proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesGopherPort: CFString](kcfnetworkproxiesgopherport.md)
  Value is a `CFNumber` indicating the port number of a gopher proxy.
- [let kCFNetworkProxiesGopherProxy: CFString](kcfnetworkproxiesgopherproxy.md)
  Value is a `CFString` object indicating the host name or IP number of a gopher proxy.
- [let kCFNetworkProxiesHTTPEnable: CFString](kcfnetworkproxieshttpenable.md)
  Value is a `CFNumber` object indicating whether an HTTP proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesHTTPPort: CFString](kcfnetworkproxieshttpport.md)
  Value is a `CFNumber` object containing the port number associated with the HTTP proxy.
- [let kCFNetworkProxiesHTTPProxy: CFString](kcfnetworkproxieshttpproxy.md)
  Value is a `CFString` object containing the HTTP proxy host name or IP number.
- [let kCFNetworkProxiesHTTPSEnable: CFString](kcfnetworkproxieshttpsenable.md)
  Value is a `CFNumber` object indicating whether an HTTPS proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesHTTPSPort: CFString](kcfnetworkproxieshttpsport.md)
  Value is a `CFNumber` object containing the port number associated with the HTTPS proxy.
- [let kCFNetworkProxiesHTTPSProxy: CFString](kcfnetworkproxieshttpsproxy.md)
  Value is a `CFString` object containing the HTTPS proxy host name or IP number.
- [let kCFNetworkProxiesRTSPEnable: CFString](kcfnetworkproxiesrtspenable.md)
  Value is a `CFNumber` object indicating whether an RTSP proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesRTSPPort: CFString](kcfnetworkproxiesrtspport.md)
  Value is a `CFNumber` object containing the port number associated with the RTSP proxy.
- [let kCFNetworkProxiesRTSPProxy: CFString](kcfnetworkproxiesrtspproxy.md)
  Value is a `CFString` object containing the RTSP proxy host name or IP number.
- [let kCFNetworkProxiesSOCKSEnable: CFString](kcfnetworkproxiessocksenable.md)
  Value is a `CFNumber` object indicating whether a SOCKS proxy is enabled. The proxy is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesSOCKSPort: CFString](kcfnetworkproxiessocksport.md)
  Value is a `CFNumber` object containing the port number associated with the SOCKS proxy.
- [let kCFNetworkProxiesSOCKSProxy: CFString](kcfnetworkproxiessocksproxy.md)
  Value is a `CFString` object containing the SOCKS proxy host name or IP number.
- [let kCFNetworkProxiesProxyAutoConfigEnable: CFString](kcfnetworkproxiesproxyautoconfigenable.md)
  Value is a `CFNumber` object indicating whether proxy autoconfiguration is enabled. Proxy autoconfiguration is enabled if the key is present and the associated value is nonzero.
- [let kCFNetworkProxiesProxyAutoConfigJavaScript: CFString](kcfnetworkproxiesproxyautoconfigjavascript.md)
  Value is a `CFString` object that contains the full JavaScript source of the ProxyAutoConfig (PAC) file.
- [let kCFNetworkProxiesProxyAutoConfigURLString: CFString](kcfnetworkproxiesproxyautoconfigurlstring.md)
  Value is a `CFString` object that contains the URL of the proxy autoconfiguration (PAC) file.
- [let kCFNetworkProxiesProxyAutoDiscoveryEnable: CFString](kcfnetworkproxiesproxyautodiscoveryenable.md)
  Value is a `CFNumber` object indicating whether proxy autodiscovery is enabled. Proxy autodiscovery is enabled if the key is present and the associated value is nonzero.

## See Also

- [func CFNetworkCopyProxiesForURL(CFURL, CFDictionary) -> Unmanaged<CFArray>](cfnetworkcopyproxiesforurl(_:_:).md)
  Returns the list of proxies that should be used to download a given URL.
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](cfnetworkcopyproxiesforautoconfigurationscript(_:_:_:).md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationscript(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkExecuteProxyAutoConfigurationURL(CFURL, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](cfnetworkcopysystemproxysettings().md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) and [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)).
- [Proxy Types](proxy-types.md)
  Constants that specify the type of proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/global-proxy-settings-constants)*