# NSBundleResourceRequestLoadingPriorityUrgent

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use Background Assets instead.

## Declaration

```swift
let NSBundleResourceRequestLoadingPriorityUrgent: Double
```

```c
extern const double NSBundleResourceRequestLoadingPriorityUrgent;
```

## Discussion

A special value for loading priority informing the system that the user cannot continue until the resources marked with the tags managed by the request are downloaded. The system will dedicate the maximum amount of capacity to completing the resource request.

## See Also

### Setting the download priority
- [var loadingPriority: Double](./nsbundleresourcerequest/loadingpriority.md)
  A hint to the system of the relative priority of the resource request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent)*