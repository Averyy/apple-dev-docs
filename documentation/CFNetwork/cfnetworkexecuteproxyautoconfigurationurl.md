# CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Downloads a proxy autoconfiguration script and executes it.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL, _ targetURL: CFURL, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource
```

#### Discussion

This function returns a run loop source that the caller should schedule. Once downloading and execution of the script has completed, the specified callback function is called.

> **Note**:  If you want to terminate the request before completion, you should invalidate the run loop source.

 If you want to terminate the request before completion, you should invalidate the run loop source.

## Parameters

- `proxyAutoConfigURL`: The URL of the autoconfiguration script.
- `targetURL`: The URL that your application intends to eventually download using the proxies.
- `cb`: A callback to be called when execution of the script is finished.
- `clientContext`: A stream context containing a client info object and optionally retain and release callbacks for that object.

## See Also

- [func CFNetworkCopyProxiesForURL(CFURL, CFDictionary) -> Unmanaged<CFArray>](cfnetworkcopyproxiesforurl(_:_:).md)
  Returns the list of proxies that should be used to download a given URL.
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](cfnetworkcopyproxiesforautoconfigurationscript(_:_:_:).md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](cfnetworkexecuteproxyautoconfigurationscript(_:_:_:_:).md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](cfnetworkcopysystemproxysettings().md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) and [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)).
- [Proxy Types](proxy-types.md)
  Constants that specify the type of proxy.
- [Global Proxy Settings Constants](global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](cfnetworkcopysystemproxysettings().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:))*