# NSBundleResourceRequestLoadingPriorityUrgent

**Framework**: Foundation  
**Kind**: var

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSBundleResourceRequestLoadingPriorityUrgent: Double
```

#### Discussion

A special value for loading priority informing the system that the user cannot continue until the resources marked with the tags managed by the request are downloaded. The system will dedicate the maximum amount of capacity to completing the resource request.

## See Also

- [var loadingPriority: Double](nsbundleresourcerequest/loadingpriority.md)
  A hint to the system of the relative priority of the resource request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent)*