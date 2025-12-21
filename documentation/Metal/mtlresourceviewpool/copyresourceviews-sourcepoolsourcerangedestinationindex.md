# copyResourceViews(sourcePool:sourceRange:destinationIndex:)

**Framework**: Metal  
**Kind**: method

Copies a range of resource views from a source view pool to a destination location in this view pool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copyResourceViews(sourcePool: any MTLResourceViewPool, sourceRange: Range<Int>, destinationIndex: Int) -> MTLResourceID
```

#### Return Value

The [`MTLResourceID`](mtlresourceid.md) of the resource view corresponding to `destinationIndex` of the copy in this resource view pool.

## Parameters

- `sourcePool`: Resource view pool from which to copy resource views.
- `sourceRange`: The range in the source resource view pool to copy.
- `destinationIndex`: The starting index in this destination view pool into which to copy the source range of resource views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceviewpool/copyresourceviews(sourcepool:sourcerange:destinationindex:))*