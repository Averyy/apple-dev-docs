# dropUpdated(info:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a validated drop moved inside the modified view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func dropUpdated(info: DropInfo) -> DropProposal?
```

## Discussion

Use this method to return a drop proposal containing the operation the delegate intends to perform at the drop [`location`](../dropinfo/location.md). The default implementation of this method returns `nil`, which tells the drop to use the last valid returned value or else [`DropOperation.copy`](../dropoperation/copy.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate/dropupdated(info:)-2mktz)*