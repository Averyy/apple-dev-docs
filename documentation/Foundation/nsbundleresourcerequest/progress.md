# progress

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A reference to the progress object associated with the specified resource request. (read-only)

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
var progress: Progress { get }
```

```objc
@property (strong, readonly) NSProgress * progress;
```

#### Discussion

This [`Progress`](../progress.md) object will begin updating after [`beginAccessingResources(completionHandler:)`](./beginaccessingresources%28completionhandler%29.md) is called.

## See Also

### Related Documentation
- [func beginAccessingResources(completionHandler: ((any Error)?) -> Void)](./beginaccessingresources%28completionhandler%29.md)
  Requests access to the resources marked with the managed tags. If any of the resources are not on the device, they are requested from the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/progress)*