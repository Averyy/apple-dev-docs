# CFNetworkCopyProxiesForURL(_:_:)

**Framework**: CFNetwork  
**Kind**: func  
**Role**: Function

Returns the list of proxies that should be used to download a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFNetworkCopyProxiesForURL(_ url: CFURL, _ proxySettings: CFDictionary) -> Unmanaged<CFArray>
```

```c
extern CFArrayRefCFNetworkCopyProxiesForURL(CFURLRef url, CFDictionaryRef proxySettings);
```

## Return Value

Returns an array of dictionaries. Each dictionary describes a single proxy. The array is ordered optimally for requesting the URL specified.

## Discussion

In general, you should try to download a URL using the first proxy in the array, try the second proxy if the first one fails, and so on.

Every proxy dictionary has an entry for `kCFProxyTypeKey`.  If the type is anything except `kCFProxyTypeAutoConfigurationURL`, the dictionary also has entries for the proxy’s host and port (under `kCFProxyHostNameKey` and `kCFProxyPortNumberKey` respectively).  If the type is `kCFProxyTypeAutoConfigurationURL`, it has an entry for `kCFProxyAutoConfigurationURLKey`.

The keys for username and password are optional and are present only if the username or password could be extracted from the information passed in (either from the URL itself or from the proxy dictionary supplied).  These APIs do not consult any external credential stores such as the Keychain.

For more information, see [CFNetwork Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132).

## Parameters

- `url`: The URL your application intends to access.
- `proxySettings`: A dictionary describing the available proxy settings. The dictionary should be in the format returned by `SystemConfiguration.framework`. (See [`kCFStreamErrorDomainSystemConfiguration`](./kcfstreamerrordomainsystemconfiguration.md) for more information.)

## See Also

### Global Proxy Configuration
- [func CFNetworkCopyProxiesForAutoConfigurationScript(CFString, CFURL, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFArray>?](./cfnetworkcopyproxiesforautoconfigurationscript%28_,_,_%29.md)
  Executes a proxy autoconfiguration script to determine the best proxy to use to retrieve a specified URL.
- [func CFNetworkExecuteProxyAutoConfigurationScript(CFString, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](./cfnetworkexecuteproxyautoconfigurationscript%28_,_,_,_%29.md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkExecuteProxyAutoConfigurationURL(CFURL, CFURL, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> CFRunLoopSource](./cfnetworkexecuteproxyautoconfigurationurl%28_,_,_,_%29.md)
  Downloads a proxy autoconfiguration script and executes it.
- [func CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>?](./cfnetworkcopysystemproxysettings%28%29.md)
  Returns a CFDictionary containing the current systemwide internet proxy settings.
- [typealias CFProxyAutoConfigurationResultCallback](./cfproxyautoconfigurationresultcallback.md)
  Callback function called when a proxy autoconfiguration computation has completed.
- [Property Keys](./property-keys.md)
  Keys for calls to property get/set functions such as [`CFReadStreamSetProperty(_:_:_:)`](../CoreFoundation/cfreadstreamsetproperty%28_,_,_%29.md) and [`CFReadStreamCopyProperty(_:_:)`](../CoreFoundation/cfreadstreamcopyproperty%28_,_%29.md).
- [Proxy Types](./proxy-types.md)
  Constants that specify the type of proxy.
- [Global Proxy Settings Constants](./global-proxy-settings-constants.md)
  Constants for keys in the global proxy settings dictionary returned by [`CFNetworkCopySystemProxySettings()`](./cfnetworkcopysystemproxysettings%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfnetworkcopyproxiesforurl(_:_:))*