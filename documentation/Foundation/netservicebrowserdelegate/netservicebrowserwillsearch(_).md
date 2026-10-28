# netServiceBrowserWillSearch(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a search is commencing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowserWillSearch(_ browser: NetServiceBrowser)
```

```objc
- (void) netServiceBrowserWillSearch:(NSNetServiceBrowser *) browser;
```

## Discussion

This message is sent to the delegate only if the underlying network layer is ready to begin a search. The delegate can use this notification to prepare its data structures to receive data.

## Parameters

- `browser`: Sender of this delegate message.

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
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](./netservicebrowser%28_,didnotsearch%29.md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](./netservicebrowserdidstopsearch%28_%29.md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserwillsearch(_:))*