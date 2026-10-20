# netServiceBrowser(_:didRemoveDomain:moreComing:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the a domain has disappeared or has become unavailable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netServiceBrowser(_ browser: NetServiceBrowser, didRemoveDomain domainString: String, moreComing: Bool)
```

```objc
- (void) netServiceBrowser:(NSNetServiceBrowser *) browser didRemoveDomain:(NSString *) domainString moreComing:(BOOL) moreComing;
```

#### Discussion

The delegate uses this message to compile a list of unavailable domains. It should wait until `moreDomainsComing` is [`false`](../../Swift/false.md) to do a bulk update of user interface elements.

## Parameters

- `browser`: Sender of this delegate message.
- `domainString`: Name of the domain that became unavailable.
- `moreComing`: [`true`](../../Swift/true.md) when `netServiceBrowser` is waiting for additional domains. [`false`](../../Swift/false.md) when there are no additional domains.

## See Also

### Using Network Service Browsers
- [func netServiceBrowser(NetServiceBrowser, didFindDomain: String, moreComing: Bool)](./netservicebrowser%28_,didfinddomain,morecoming%29.md)
  Tells the delegate the sender found a domain.
- [func netServiceBrowser(NetServiceBrowser, didFind: NetService, moreComing: Bool)](./netservicebrowser%28_,didfind,morecoming%29.md)
  Tells the delegate the sender found a service.
- [func netServiceBrowser(NetServiceBrowser, didRemove: NetService, moreComing: Bool)](./netservicebrowser%28_,didremove,morecoming%29.md)
  Tells the delegate a service has disappeared or has become unavailable.
- [func netServiceBrowserWillSearch(NetServiceBrowser)](./netservicebrowserwillsearch%28_%29.md)
  Tells the delegate that a search is commencing.
- [func netServiceBrowser(NetServiceBrowser, didNotSearch: [String : NSNumber])](./netservicebrowser%28_,didnotsearch%29.md)
  Tells the delegate that a search was not successful.
- [func netServiceBrowserDidStopSearch(NetServiceBrowser)](./netservicebrowserdidstopsearch%28_%29.md)
  Tells the delegate that a search was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowserdelegate/netservicebrowser(_:didremovedomain:morecoming:))*