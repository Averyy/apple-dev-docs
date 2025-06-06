# endAccessingResources()

**Framework**: Foundation  
**Kind**: method

Informs the system that you have finished accessing the resources marked with the tags managed by the request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func endAccessingResources()
```

#### Discussion

Call this method as soon as you have finished using the tags managed by this request. If needed, this method will be called by the system when the resource request object is deallocated.

> ❗ **Important**:  The callback from [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) or [`conditionallyBeginAccessingResources(completionHandler:)`](nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:).md) must have completed before calling [`endAccessingResources()`](nsbundleresourcerequest/endaccessingresources().md).

 The callback from [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) or [`conditionallyBeginAccessingResources(completionHandler:)`](nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:).md) must have completed before calling [`endAccessingResources()`](nsbundleresourcerequest/endaccessingresources().md).

## See Also

- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.
- [func conditionallyBeginAccessingResources(completionHandler: (Bool) -> Void)](nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:).md)
  Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/endaccessingresources())*