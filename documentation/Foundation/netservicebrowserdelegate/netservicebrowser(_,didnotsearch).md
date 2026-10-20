# netServiceBrowser(_:didNotSearch:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a search was not successful.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didNotSearch errorDict: [String : NSNumber])
```

```objc
- (void) netServiceBrowser:(NSNetServiceBrowser *) browser didNotSearch:(NSDictionary<NSString *,NSNumber *> *) errorDict;
```

## Parameters

- `browser`: Sender of this delegate message.
- `errorDict`: Dictionary with the reasons the search was unsuccessful. Use the dictionary keys [`errorCode`](../netservice/errorcode-swift.type.property.md) and [`errorDomain`](../netservice/errordomain.md) to retrieve the error information from the dictionary.

## See Also

### Using Network Service Browsers
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](./netservicebrowser%28_,didfinddomain,morecoming%29.md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didRemoveDomain: String, moreComing: Bool)](./netservicebrowser%28_,didremovedomain,morecoming%29.md)
  Tells the delegate the a domain has disappeared or has become unavailable.
- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](./netservicebrowser%28_,didfind,morecoming%29.md)
  Tells the delegate the sender found a service.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](./netservicebrowser%28_,didremove,morecoming%29.md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](./netservicebrowserwillsearch%28_%29.md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](./netservicebrowserdidstopsearch%28_%29.md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didnotsearch:))*