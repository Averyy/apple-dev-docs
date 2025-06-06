# conditionallyBeginAccessingResources(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func conditionallyBeginAccessingResources() async -> Bool
```

#### Discussion

If the resources marked with the tags managed by the request are already on the device, you can start accessing them as soon as the completion handler is called with `resourcesAvailable` set to [`true`](https://developer.apple.com/documentation/swift/true). If all of the resources are not already available, you need to call [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) to download them from the App Store.

> ❗ **Important**:  If `resourcesAvailable` is [`true`](https://developer.apple.com/documentation/swift/true), do not call [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md). You must call this method or [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) before accessing any resources marked with the tags managed by the request.

 If `resourcesAvailable` is [`true`](https://developer.apple.com/documentation/swift/true), do not call [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md). You must call this method or [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) before accessing any resources marked with the tags managed by the request.

## Parameters

- `completionHandler`: The block takes the following parameter:

## See Also

- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.
- [func endAccessingResources()](nsbundleresourcerequest/endaccessingresources.md)
  Informs the system that you have finished accessing the resources marked with the tags managed by the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:))*