# endAccessingResources()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Informs the system that you have finished accessing the resources marked with the tags managed by the request.

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
func endAccessingResources()
```

```objc
- (void) endAccessingResources;
```

#### Discussion

Call this method as soon as you have finished using the tags managed by this request. If needed, this method will be called by the system when the resource request object is deallocated.

> ❗ **Important**:  The callback from [`beginAccessingResources(completionHandler:)`](./beginaccessingresources%28completionhandler%29.md) or [`conditionallyBeginAccessingResources(completionHandler:)`](./conditionallybeginaccessingresources%28completionhandler%29.md) must have completed before calling [`endAccessingResources()`](./endaccessingresources%28%29.md).

## See Also

### Requesting resources
- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](./beginaccessingresources%28completionhandler%29.md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.
- [func conditionallyBeginAccessingResources(completionHandler: (Bool) -> Void)](./conditionallybeginaccessingresources%28completionhandler%29.md)
  Checks whether the resources marked with the tags managed by the request are already on the device. If all of the resources are on the device, you can begin accessing those resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/endaccessingresources())*