# conditionallyBeginAccessingResources(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.

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
func conditionallyBeginAccessingResources(completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func conditionallyBeginAccessingResources() async -> Bool
```

```objc
- (void) conditionallyBeginAccessingResourcesWithCompletionHandler:(void (^)(BOOL resourcesAvailable)) completionHandler;
```

## Discussion

If the resources marked with the tags managed by the request are already on the device, you can start accessing them as soon as the completion handler is called with `resourcesAvailable` set to [`true`](../../Swift/true.md). If all of the resources are not already available, you need to call [`beginAccessingResources(completionHandler:)`](./beginaccessingresources%28completionhandler%29.md) to download them from the App Store.

> ❗ **Important**:  If `resourcesAvailable` is [`true`](../../Swift/true.md), do not call [`beginAccessingResources(completionHandler:)`](./beginaccessingresources%28completionhandler%29.md). You must call this method or [`beginAccessingResources(completionHandler:)`](./beginaccessingresources%28completionhandler%29.md) before accessing any resources marked with the tags managed by the request.

## Parameters

- `completionHandler`: A block called when the availability of the resources has been checked.

  The block takes the following parameter:

  - **resourcesAvailable**: Returns [`true`](../../Swift/true.md) if all of the resources marked with the tags managed by the request are already on the device. Returns [`false`](../../Swift/false.md) if any of the resources are not on the device.

## See Also

### Requesting resources
- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](./beginaccessingresources%28completionhandler%29.md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.
- [func endAccessingResources()](./endaccessingresources%28%29.md)
  Informs the system that you have finished accessing the resources marked with the tags managed by the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler:))*