# commissioning(_:succeededForNodeID:metrics:context:)

**Framework**: Matter  
**Kind**: method

Notification that commissioning has succeeded.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
optional func commissioning(_ commissioning: MTRCommissioningOperation, succeededForNodeID nodeID: NSNumber, metrics: MTRMetrics, context: [String : Any])
```

#### Discussion

If supported, this selector will be used in preference to commissioning:succeededForNodeID:metrics:.

The context parameter is a dictionary with NSString keys and values of type id. The supported keys are defined above in this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:succeededfornodeid:metrics:context:))*