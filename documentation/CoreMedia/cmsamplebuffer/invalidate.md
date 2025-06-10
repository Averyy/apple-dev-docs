# invalidate()

**Framework**: Core Media  
**Kind**: method

Invalidates a sample buffer by calling its invalidation handler.

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
func invalidate() throws
```

#### Discussion

You can’t use a sample buffer after invalidating it; all of its accessors throw errors.

> ❗ **Important**:  Don’t invalidate a sample buffer that another process is accessing concurrently.

## See Also

- [var isValid: Bool](cmsamplebuffer/isvalid.md)
  A Boolean value that indicates whether the sample buffer is valid.
- [func setInvalidateHandler((CMSampleBuffer) throws -> Void) throws](cmsamplebuffer/setinvalidatehandler(_:).md)
  Sets a closure for the sample buffer to call when it’s invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/invalidate())*