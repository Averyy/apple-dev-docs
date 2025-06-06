# progress

**Framework**: Foundation  
**Kind**: property

A reference to the progress object associated with the specified resource request. (read-only)

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var progress: Progress { get }
```

#### Discussion

This [`Progress`](progress.md) object will begin updating after [`beginAccessingResources(completionHandler:)`](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md) is called.

## See Also

- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](nsbundleresourcerequest/beginaccessingresources(completionhandler:).md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/progress)*