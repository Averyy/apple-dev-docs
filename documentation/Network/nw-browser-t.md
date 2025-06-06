# nw_browser_t

**Framework**: Network  
**Kind**: typealias

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

## Topics

### Essentials
- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells the user why the app is requesting access to the local network.
### Browsing for Services
- [func nw_browser_create(nw_browse_descriptor_t, nw_parameters_t?) -> nw_browser_t](nw_browser_create(_:_:).md)
  Initializes a browser with a type of service to discover.
- [typealias nw_browse_descriptor_t](nw_browse_descriptor_t.md)
  A service description used to discover Bonjour services.
- [func nw_browser_set_queue(nw_browser_t, dispatch_queue_t)](nw_browser_set_queue(_:_:).md)
  Sets the queue on which all browser events will be delivered.
- [func nw_browser_start(nw_browser_t)](nw_browser_start(_:).md)
  Starts browsing for services.
- [func nw_browser_set_browse_results_changed_handler(nw_browser_t, nw_browser_browse_results_changed_handler_t?)](nw_browser_set_browse_results_changed_handler(_:_:).md)
  Sets the handler to receive updates about discovered services.
- [typealias nw_browser_browse_results_changed_handler_t](nw_browser_browse_results_changed_handler_t.md)
  A handler that delivers updates about discovered services.
- [typealias nw_browse_result_t](nw_browse_result_t.md)
  A discovered service and metadata about the service.
### Managing Browsers
- [func nw_browser_set_state_changed_handler(nw_browser_t, nw_browser_state_changed_handler_t?)](nw_browser_set_state_changed_handler(_:_:).md)
  Sets a handler to receive browser state updates.
- [typealias nw_browser_state_changed_handler_t](nw_browser_state_changed_handler_t.md)
  A handler that delivers browser state updates with associated errors.
- [struct nw_browser_state_t](nw_browser_state_t.md)
  States indicating whether a browser is able to discover services.
- [func nw_browser_cancel(nw_browser_t)](nw_browser_cancel(_:).md)
  Stops browsing for services.
### Inspecting Browsers
- [func nw_browser_copy_browse_descriptor(nw_browser_t) -> nw_browse_descriptor_t](nw_browser_copy_browse_descriptor(_:).md)
  Accesses the service descriptor with which the browser was created.
- [func nw_browser_copy_parameters(nw_browser_t) -> nw_parameters_t](nw_browser_copy_parameters(_:).md)
  Accesses the parameters with which the browser was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_browser_t)*