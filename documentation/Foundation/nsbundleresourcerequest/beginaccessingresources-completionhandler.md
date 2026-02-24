# beginAccessingResources(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func beginAccessingResources() async throws
```

#### Discussion

After calling this method, the resource request downloads any on-demand resources not already on the device. When all the resources are downloaded, they are marked as non-purgeable. The resources are not available to the app until the completion handler is called with no error.

> ❗ **Important**:  You must call this method or [`conditionallyBeginAccessingResources(completionHandler:)`](nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:).md) before accessing any resources marked with the tags managed by the request.

## Parameters

- `completionHandler`: A block called when the resources have finished downloading or if an error occurs. The resources are not available until the completion handler is called with `error` set to `nil`. The block takes the following parameter: - **error**: Set to `nil` if the resources are downloaded successfully; otherwise this parameter holds an [`NSError`](nserror.md) object describing the problem that occurred. Errors are usually due to a lack of free space or problems connecting with the App Store.

## See Also

- [func conditionallyBeginAccessingResources(completionHandler: (Bool) -> Void)](nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:).md)
  Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.
- [func endAccessingResources()](nsbundleresourcerequest/endaccessingresources.md)
  Informs the system that you have finished accessing the resources marked with the tags managed by the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/beginaccessingresources(completionhandler:))*