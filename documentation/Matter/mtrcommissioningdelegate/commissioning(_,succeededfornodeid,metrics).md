# commissioning(_:succeededForNodeID:metrics:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
optional func commissioning(_ commissioning: MTRCommissioningOperation, succeededForNodeID nodeID: NSNumber, metrics: MTRMetrics)
```

```objc
- (void) commissioning:(MTRCommissioningOperation *) commissioning succeededForNodeID:(NSNumber *) nodeID metrics:(MTRMetrics *) metrics;
```

#### Discussion

This selector will not be used if commissioning:succeededForNodeID:metrics:context: is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:succeededfornodeid:metrics:))*