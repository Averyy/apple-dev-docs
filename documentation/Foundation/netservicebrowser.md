# NetServiceBrowser

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A network service browser that finds published services on a network using multicast DNS.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_browser_t in Network framework instead

## Declaration

```swift
class NetServiceBrowser
```

```objc
@interface NSNetServiceBrowser : NSObject
```

## Overview

Services can range from standard services, such as HTTP and FTP, to custom services defined by other applications. You can use a network service browser in your code to obtain the list of accessible domains and then to obtain an [`NetService`](./netservice.md) object for each discovered service. Each network service browser performs one search at a time, so if you want to perform multiple simultaneous searches, use multiple network service browsers.

A network service browser performs all searches asynchronously using the current run loop to execute the search in the background. Results from a search are returned through the associated delegate object, which your client application must provide. Searching proceeds in the background until the object receives a [`stop()`](./netservicebrowser/stop%28%29.md) message.

To use an `NSNetServiceBrowser` object to search for services, allocate it, initialize it, and assign a delegate. (If you wish, you can also use the [`schedule(in:forMode:)`](./netservicebrowser/schedule%28in,formode%29.md) and [`remove(from:forMode:)`](./netservicebrowser/remove%28from,formode%29.md) methods to execute searches on a run loop other than the current one.) Once your object is ready, you begin by gathering the list of accessible domains using either the [`searchForRegistrationDomains()`](./netservicebrowser/searchforregistrationdomains%28%29.md) or [`searchForBrowsableDomains()`](./netservicebrowser/searchforbrowsabledomains%28%29.md) methods. From the list of returned domains, you can pick one and use the [`searchForServices(ofType:inDomain:)`](./netservicebrowser/searchforservices%28oftype,indomain%29.md) method to search for services in that domain.

The `NSNetServiceBrowser` class provides two ways to search for domains. In most cases, your client should use the [`searchForRegistrationDomains()`](./netservicebrowser/searchforregistrationdomains%28%29.md) method to search only for local domains to which the host machine has registration authority. This is the preferred method for accessing domains as it guarantees that the host machine can connect to services in the returned domains. Access to domains outside this list may be more limited.

## Topics

### Creating Network Service Browsers
- [init()](./netservicebrowser/init%28%29.md)
  Initializes an allocated [`NetServiceBrowser`](./netservicebrowser.md) object.
### Configuring Network Service Browsers
- [var delegate: (any NetServiceBrowserDelegate)?](./netservicebrowser/delegate.md)
  The delegate object for this instance.
- [var includesPeerToPeer: Bool](./netservicebrowser/includespeertopeer.md)
  Whether to browse over peer-to-peer Bluetooth and Wi-Fi, if available.
### Using Network Service Browsers
- [func searchForBrowsableDomains()](./netservicebrowser/searchforbrowsabledomains%28%29.md)
  Initiates a search for domains visible to the host. This method returns immediately.
- [func searchForRegistrationDomains()](./netservicebrowser/searchforregistrationdomains%28%29.md)
  Initiates a search for domains in which the host may register services.
- [func searchForServices(ofType: String, inDomain: String)](./netservicebrowser/searchforservices%28oftype,indomain%29.md)
  Starts a search for services of a particular type within a specific domain.
- [func stop()](./netservicebrowser/stop%28%29.md)
  Halts a currently running search or resolution.
### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./netservicebrowser/schedule%28in,formode%29.md)
  Adds the receiver to the specified run loop.
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](./netservicebrowser/remove%28from,formode%29.md)
  Removes the receiver from the specified run loop.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Service Discovery
- [protocol NetServiceBrowserDelegate](./netservicebrowserdelegate.md)
  The interface a net service browser uses to inform a delegate about the state of service discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser)*