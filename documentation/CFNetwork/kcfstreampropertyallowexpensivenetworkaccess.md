# kCFStreamPropertyAllowExpensiveNetworkAccess

**Framework**: CFNetwork  
**Kind**: var  
**Role**: Global Variable

A Boolean value that indicates whether connections may use a network interface that the system considers expensive.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let kCFStreamPropertyAllowExpensiveNetworkAccess: CFString
```

```c
extern CFStringRef const kCFStreamPropertyAllowExpensiveNetworkAccess;
```

#### Discussion

The default value is [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) and allows the use of expensive network interfaces. Set this property to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) to disallow the use of expensive network interfaces. For more information about expensive network interfaces, see [`allowsExpensiveNetworkAccess`](../Foundation/urlsessionconfiguration/allowsexpensivenetworkaccess.md).

## See Also

### Constants
- [let kCFHTTPVersion3_0: CFString](./kcfhttpversion3_0.md)
  HTTP version 3.0.
- [let kCFStreamNetworkServiceTypeAVStreaming: CFString](./kcfstreamnetworkservicetypeavstreaming.md)
  A multimedia audio and video streaming service.
- [let kCFStreamNetworkServiceTypeResponsiveAV: CFString](./kcfstreamnetworkservicetyperesponsiveav.md)
  A responsive, time-sensitive, multimedia audio and video service.
- [let kCFStreamNetworkServiceTypeResponsiveData: CFString](./kcfstreamnetworkservicetyperesponsivedata.md)
  A responsive, time-sensitive data service.
- [let kCFStreamPropertyAllowConstrainedNetworkAccess: CFString](./kcfstreampropertyallowconstrainednetworkaccess.md)
  A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.
- [let kCFStreamPropertyConnectionIsExpensive: CFString](./kcfstreampropertyconnectionisexpensive.md)
  A Boolean value that indicates if the connection is using a network interface that the system considers expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyallowexpensivenetworkaccess)*