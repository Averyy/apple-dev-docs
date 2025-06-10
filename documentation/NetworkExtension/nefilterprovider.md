# NEFilterProvider

**Framework**: Network Extension  
**Kind**: class

An abstract base class shared by content filters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterProvider
```

#### Overview

A Network Content Filter is made up of two Filter Provider extensions:

The  examines network content as it passes through the network stack on the device and decides if the network content should be blocked or allowed to pass on to its final destination.

Because the Filter Data Provider extension has access to all of the network content flowing through the device, it runs in a very restrictive sandbox. The sandbox prevents the Filter Data Provider extension from moving network content outside of its address space by blocking all network access, IPC, and disk write operations.

The Filter Data Provider extension is implemented by creating a custom subclass of the [`NEFilterDataProvider`](nefilterdataprovider.md) class.

The  is responsible for feeding information to the Filter Data Provider extension so that the Filter Data Provider extension can do its job.

For example, the Filter Control Provider extension can be notified by the Filter Data Provider extension that it does not have enough information to make a decision about a particular flow of network content. The Filter Control Provider extension can then download more filtering rules from a server and write the rules to a location where the Filter Data Provider can access them.

The Filter Control Provider extension is implemented by creating a custom subclass of the [`NEFilterControlProvider`](nefiltercontrolprovider.md) class.

> ❗ **Important**:  To use the [`NEFilterProvider`](nefilterprovider.md) class, you must enable the Network Extensions capability in Xcode and select the Content Filter capability. See [`Configure network extensions`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

##### Subclassing Notes

`NEFilterProvider` should not be subclassed directly. Instead, you should create subclasses of `NEFilterProvider’s` subclasses and override the following methods:

###### Methods to Override

- [`startFilter(completionHandler:)`](nefilterprovider/startfilter(completionhandler:).md)
- [`stopFilter(with:completionHandler:)`](nefilterprovider/stopfilter(with:completionhandler:).md)

## Topics

### Managing the filter life cycle
- [func startFilter(completionHandler: ((any Error)?) -> Void)](nefilterprovider/startfilter(completionhandler:).md)
  Start the filter.
- [func stopFilter(with: NEProviderStopReason, completionHandler: () -> Void)](nefilterprovider/stopfilter(with:completionhandler:).md)
  Stop the filter.
### Getting the filter configuration
- [var filterConfiguration: NEFilterProviderConfiguration](nefilterprovider/filterconfiguration.md)
  An [`NEFilterProviderConfiguration`](nefilterproviderconfiguration.md) object containing the current filter configuration.
### Receiving reports
- [func handle(NEFilterReport)](nefilterprovider/handle(_:).md)
  Receives a report from the framework.
### Handling errors
- [let NEFilterErrorDomain: String](nefiltererrordomain.md)
  The domain for errors resulting from calls to the filter manager.
- [enum NEFilterManagerError](nefiltermanagererror.md)
  Error codes specific to filter managers.

## Relationships

### Inherits From
- [NEProvider](neprovider.md)
### Inherited By
- [NEFilterControlProvider](nefiltercontrolprovider.md)
- [NEFilterDataProvider](nefilterdataprovider.md)
- [NEFilterPacketProvider](nefilterpacketprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEFilterDataProvider](nefilterdataprovider.md)
  The principal class for a filter data provider extension.
- [class NEFilterControlProvider](nefiltercontrolprovider.md)
  The principal class for a filter control provider extension.
- [class NEFilterPacketProvider](nefilterpacketprovider.md)
  A filter provider that evaluates network packets and decides whether to block, allow, or delay the packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider)*