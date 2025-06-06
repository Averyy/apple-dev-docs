# isValid

**Framework**: Core Media  
**Kind**: property

A Boolean value that indicates whether the sample buffer is valid.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isValid: Bool { get }
```

## See Also

- [func setInvalidateHandler((CMSampleBuffer) throws -> Void) throws](cmsamplebuffer/setinvalidatehandler(_:).md)
  Sets a closure for the sample buffer to call when it’s invalidated.
- [func invalidate() throws](cmsamplebuffer/invalidate.md)
  Invalidates a sample buffer by calling its invalidation handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/isvalid)*