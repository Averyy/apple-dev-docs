# nw_browser_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

An object you use to browse for available network services.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias nw_browser_t = any OS_nw_browser
```

```c
typedef NSObject<OS_nw_browser> * nw_browser_t;
```

## Topics

### Essentials
- [NSBonjourServices](../BundleResources/information-property-list/nsbonjourservices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/information-property-list/nslocalnetworkusagedescription.md)
  A message that tells people why the app is requesting access to the local network.
### Browsing for Services
- [func nw_browser_create(nw_browse_descriptor_t, nw_parameters_t?) -> nw_browser_t](./nw_browser_create%28_,_%29.md)
  Initializes a browser with a type of service to discover.
- [typealias nw_browse_descriptor_t](./nw_browse_descriptor_t.md)
  A service description used to discover Bonjour services.
- [func nw_browser_set_queue(nw_browser_t, dispatch_queue_t)](./nw_browser_set_queue%28_,_%29.md)
  Sets the queue on which all browser events will be delivered.
- [func nw_browser_start(nw_browser_t)](./nw_browser_start%28_%29.md)
  Starts browsing for services.
- [func nw_browser_set_browse_results_changed_handler(nw_browser_t, nw_browser_browse_results_changed_handler_t?)](./nw_browser_set_browse_results_changed_handler%28_,_%29.md)
  Sets the handler to receive updates about discovered services.
- [typealias nw_browser_browse_results_changed_handler_t](./nw_browser_browse_results_changed_handler_t.md)
  A handler that delivers updates about discovered services.
- [typealias nw_browse_result_t](./nw_browse_result_t.md)
  A discovered service and metadata about the service.
### Managing Browsers
- [func nw_browser_set_state_changed_handler(nw_browser_t, nw_browser_state_changed_handler_t?)](./nw_browser_set_state_changed_handler%28_,_%29.md)
  Sets a handler to receive browser state updates.
- [typealias nw_browser_state_changed_handler_t](./nw_browser_state_changed_handler_t.md)
  A handler that delivers browser state updates with associated errors.
- [struct nw_browser_state_t](./nw_browser_state_t.md)
  States indicating whether a browser is able to discover services.
- [func nw_browser_cancel(nw_browser_t)](./nw_browser_cancel%28_%29.md)
  Stops browsing for services.
### Inspecting Browsers
- [func nw_browser_copy_browse_descriptor(nw_browser_t) -> nw_browse_descriptor_t](./nw_browser_copy_browse_descriptor%28_%29.md)
  Accesses the service descriptor with which the browser was created.
- [func nw_browser_copy_parameters(nw_browser_t) -> nw_parameters_t](./nw_browser_copy_parameters%28_%29.md)
  Accesses the parameters with which the browser was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_browser_t)*