# CFProxyAutoConfigurationResultCallback

**Framework**: CFNetwork  
**Kind**: typealias

Callback function called when a proxy autoconfiguration computation has completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias CFProxyAutoConfigurationResultCallback = (UnsafeMutableRawPointer, CFArray, CFError?) -> Void
```

## Parameters

- `client`: The client reference originally passed in the   parameter of the   or   call that triggered this callback.
- `proxyList`: The list of proxies returned by the autoconfiguration script. This list is in a format suitable for passing to   (with the added guarantee that no entries will ever be autoconfiguration URL entries). If an error occurs, this value will be  .
- `error`: An error object that indicates any error that may have occurred. If no error occurred, this value will be NULL.

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
- [Property Keys](property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamSetProperty(_:_:_:)) and [`CFReadStreamCopyProperty(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFReadStreamCopyProperty(_:_:)).
- [Proxy Types](proxy-types.md)
  Constants that specify the type of proxy.
- [Global Proxy Settings Constants](global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](cfnetworkcopysystemproxysettings().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfproxyautoconfigurationresultcallback)*