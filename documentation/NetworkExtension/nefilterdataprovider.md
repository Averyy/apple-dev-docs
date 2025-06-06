# NEFilterDataProvider

**Framework**: Network Extension  
**Kind**: class

The principal class for a filter data provider extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class NEFilterDataProvider
```

#### Overview

Network content is delivered to the Filter Data Provider in the form of [`NEFilterFlow`](nefilterflow.md) objects. Each [`NEFilterFlow`](nefilterflow.md) object corresponds to a network connection opened by an application running on the device. The Filter Data Provider can choose to pass or block the data when it receives a new flow, or it can ask the system to see more of the flow’s data in either the outbound or inbound direction before making a pass or block decision.

In addition to passing or blocking network data, the Filter Data Provider can tell the system that it needs more information before it can make a decision about a particular flow of data. The system will then ask the Filter Control Provider to update the current set of rules and place them in a location on disk that is readable from the Filter Data Provider extension.

When a [`NEFilterFlow`](nefilterflow.md) object is originated from a WebKit browser object, the Filter Data Provider can affect the user experience in the following ways:

- If the Filter Data Provider chooses to block the web page, then a special “block” page is displayed in the WebKit browser object informing the user that their attempt to access the content was blocked. The Filter Data Provider can choose to add a link to this block page, giving the user the option of requesting access to the content.
- If the Filter Data Provider chooses to allow the web page, then it can also specify that a string be appended to the web page URL. This allows the Filter Data Provider to direct the WebKit browser object to a “safe” version of the web page.

To protect the user’s privacy, the Filter Data Provider extension sandbox prevents the extension from moving network content outside of its address space.

> ❗ **Important**:  To use the [`handleNewFlow(_:)`](nefilterdataprovider/handlenewflow(_:).md) method, you must enable the Network Extensions capability in Xcode and select the Content Filter capability. See [`Configure network extensions`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

 To use the [`handleNewFlow(_:)`](nefilterdataprovider/handlenewflow(_:).md) method, you must enable the Network Extensions capability in Xcode and select the Content Filter capability. See [`Configure network extensions`](https://developer.apple.comhttp://help.apple.com/xcode/mac/current/#/dev0b2ef6f08).

##### Creating a Filter Data Provider Extension

Filter Data Providers run as App Extensions for the `com.apple.networkextension.filter-data` extension point.

To create a Filter Data Provider extension, first create a new App Extension target in your project.

For an example of an Xcode build target for this app extension, see the [`SimpleTunnel: Customized Networking Using the NetworkExtension Framework`](https://developer.apple.comhttps://developer.apple.com/library/archive/samplecode/SimpleTunnel/Introduction/Intro.html#//apple_ref/doc/uid/TP40016140) sample code project.

Once you have a Filter Data Provider extension target, create a subclass of `NEFilterDataProvider`. Then set the `NSExtensionPrincipalClass` key in the the extension’s `Info.plist` to the name of your subclass.

If it is not done already, set the `NSExtensionPointIdentifier` key in the extension’s `Info.plist` to `com.apple.networkextension.filter-data`.

Here is an example of the `NSExtension` dictionary in a Filter Data Provider extension’s `Info.plist`:

```xml
<key>NSExtension</key>
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.networkextension.filter-data</string>
    <key>NSExtensionPrincipalClass</key>
    <string>MyCustomFilterDataProvider</string>
</dict>
```

Finally, add your Filter Data Provider extension target to your app’s Embed App Extensions build phase.

##### Subclassing Notes

To create a Filter Data Provider extension, you must first create a subclass of `NEFilterDataProvider` and override the methods listed below.

###### Methods to Override

- [`handleNewFlow(_:)`](nefilterdataprovider/handlenewflow(_:).md)
- [`handleInboundData(from:readBytesStartOffset:readBytes:)`](nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:).md)
- [`handleOutboundData(from:readBytesStartOffset:readBytes:)`](nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:).md)
- [`handleInboundDataComplete(for:)`](nefilterdataprovider/handleinbounddatacomplete(for:).md)
- [`handleOutboundDataComplete(for:)`](nefilterdataprovider/handleoutbounddatacomplete(for:).md)
- [`handleRemediation(for:)`](nefilterdataprovider/handleremediation(for:).md)
- [`handleRulesChanged()`](nefilterdataprovider/handleruleschanged().md)

## Topics

### Filtering network content
- [func handleNewFlow(NEFilterFlow) -> NEFilterNewFlowVerdict](nefilterdataprovider/handlenewflow(_:).md)
  Make a filtering decision for a newly-created flow of network content.
- [func handleInboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of inbound data.
- [enum NEFilterDataAttribute](nefilterdataattribute.md)
  Attribute flags that describe the data handled by a filter.
- [func handleOutboundData(from: NEFilterFlow, readBytesStartOffset: Int, readBytes: Data) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddata(from:readbytesstartoffset:readbytes:).md)
  Make a filtering decision about a chunk of outbound data.
- [func handleInboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleinbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the inbound data for a flow.
- [func handleOutboundDataComplete(for: NEFilterFlow) -> NEFilterDataVerdict](nefilterdataprovider/handleoutbounddatacomplete(for:).md)
  Make a filtering decision after seeing all of the outbound data for a flow.
### Handling remediation
- [func handleRemediation(for: NEFilterFlow) -> NEFilterRemediationVerdict](nefilterdataprovider/handleremediation(for:).md)
  Handle a remediation request.
### Handling rule updates
- [func handleRulesChanged()](nefilterdataprovider/handleruleschanged.md)
  Handle a rules changed event.
### Changing filter settings
- [func apply(NEFilterSettings?, completionHandler: ((any Error)?) -> Void)](nefilterdataprovider/apply(_:completionhandler:).md)
  Applies a set of filtering rules associated with the provider and changes the default filtering action.
- [class NEFilterSettings](nefiltersettings.md)
  The rules and other settings that define the operation of a filter.
### Resuming data flows
- [func resumeFlow(NEFilterFlow, with: NEFilterVerdict)](nefilterdataprovider/resumeflow(_:with:).md)
  Resumes a previously-paused flow.
### Updating filter verdicts
- [func update(NEFilterSocketFlow, using: NEFilterDataVerdict, for: NETrafficDirection)](nefilterdataprovider/update(_:using:for:).md)
  Updates the verdict for a flow outside the context of any filter data provider callback.

## Relationships

### Inherits From
- [NEFilterProvider](nefilterprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEFilterControlProvider](nefiltercontrolprovider.md)
  The principal class for a filter control provider extension.
- [class NEFilterPacketProvider](nefilterpacketprovider.md)
  A filter provider that evaluates network packets and decides whether to block, allow, or delay the packets.
- [class NEFilterProvider](nefilterprovider.md)
  An abstract base class shared by content filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider)*