# kCFStreamPropertyAllowConstrainedNetworkAccess

**Framework**: CFNetwork  
**Kind**: var

A Boolean value that indicates whether connections may use the network when the user has specified Low Data Mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let kCFStreamPropertyAllowConstrainedNetworkAccess: CFString
```

#### Discussion

The default value is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) and allows the use of constrained interfaces. Set this property to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) to disallow the use of constrained interfaces. For more information about constrained interfaces, see [`allowsConstrainedNetworkAccess`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/allowsConstrainedNetworkAccess).

## See Also

- [let kCFHTTPVersion3_0: CFString](kcfhttpversion3_0.md)
  HTTP version 3.0.
- [let kCFStreamNetworkServiceTypeAVStreaming: CFString](kcfstreamnetworkservicetypeavstreaming.md)
  A multimedia audio and video streaming service.
- [let kCFStreamNetworkServiceTypeResponsiveAV: CFString](kcfstreamnetworkservicetyperesponsiveav.md)
  A responsive, time-sensitive, multimedia audio and video service.
- [let kCFStreamNetworkServiceTypeResponsiveData: CFString](kcfstreamnetworkservicetyperesponsivedata.md)
  A responsive, time-sensitive data service.
- [let kCFStreamPropertyAllowExpensiveNetworkAccess: CFString](kcfstreampropertyallowexpensivenetworkaccess.md)
  A Boolean value that indicates whether connections may use a network interface that the system considers expensive.
- [let kCFStreamPropertyConnectionIsExpensive: CFString](kcfstreampropertyconnectionisexpensive.md)
  A Boolean value that indicates if the connection is using a network interface that the system considers expensive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyallowconstrainednetworkaccess)*