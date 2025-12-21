# handleBDXTransferSessionEnd(forNodeID:controller:metrics:error:)

**Framework**: Matter  
**Kind**: method

Notify the delegate when a BDX Session ends for some node.  The controller identifies the fabric the node is on, and the nodeID identifies the node within that fabric.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- tvOS 26.1+
- visionOS 26.1+
- watchOS 26.1+

## Declaration

```swift
optional func handleBDXTransferSessionEnd(forNodeID nodeID: NSNumber, controller: MTRDeviceController, metrics: MTRMetrics, error: (any Error)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handlebdxtransfersessionend(fornodeid:controller:metrics:error:))*