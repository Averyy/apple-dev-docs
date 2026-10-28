# netServiceBrowserDidStopSearch(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a search was stopped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowserDidStopSearch(_ browser: NetServiceBrowser)
```

```objc
- (void) netServiceBrowserDidStopSearch:(NSNetServiceBrowser *) browser;
```

## Discussion

When `netServiceBrowser` receives a [`stop()`](../netservicebrowser/stop%28%29.md) message from its client, `netServiceBrowser` sends a `netServiceBrowserDidStopSearch:` message to its delegate. The delegate then performs any necessary cleanup.

## Parameters

- `browser`: Sender of this delegate message.

## See Also

### Related Documentation
- [func stop()](../netservicebrowser/stop%28%29.md)
  Halts a currently running search or resolution.
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
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](./netservicebrowser%28_,didnotsearch%29.md)
  Tells the delegate that a search was not successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowserdidstopsearch(_:))*