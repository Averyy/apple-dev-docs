# loadingPriority

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A hint to the system of the relative priority of the resource request.

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
var loadingPriority: Double { get set }
```

```objc
@property double loadingPriority;
```

## Discussion

Possible values are between `0.0` and `1.0` or the special constant [`NSBundleResourceRequestLoadingPriorityUrgent`](../nsbundleresourcerequestloadingpriorityurgent.md). The default is `0.5`. The system will attempt to give higher priority to requests with higher values. You can change the priority at any time, including during downloading of the managed resources.

## See Also

### Setting the download priority
- [let NSBundleResourceRequestLoadingPriorityUrgent: Double](../nsbundleresourcerequestloadingpriorityurgent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/loadingpriority)*