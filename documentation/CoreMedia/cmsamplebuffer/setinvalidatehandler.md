# setInvalidateHandler(_:)

**Framework**: Core Media  
**Kind**: method

Sets a closure for the sample buffer to call when it’s invalidated.

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
func setInvalidateHandler(_ body: @escaping (CMSampleBuffer) throws -> Void) throws
```

#### Discussion

A sample buffer can only have one invalidation handler.

## Parameters

- `body`: The invalidation handler.

## See Also

- [var isValid: Bool](cmsamplebuffer/isvalid.md)
  A Boolean value that indicates whether the sample buffer is valid.
- [func invalidate() throws](cmsamplebuffer/invalidate.md)
  Invalidates a sample buffer by calling its invalidation handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/setinvalidatehandler(_:))*