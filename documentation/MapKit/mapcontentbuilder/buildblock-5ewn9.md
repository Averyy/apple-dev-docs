# buildBlock(_:)

**Framework**: MapKit  
**Kind**: method

Creates a map content block that contains a single content result.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func buildBlock<C>(_ content: C) -> C where C : MapContent
```

#### Return Value

Returns the [`MapContent`](mapcontent.md) with the single element you provided.

## Parameters

- `content`: The view content to add to the block.

## See Also

- [static func buildBlock() -> EmptyMapContent](mapcontentbuilder/buildblock.md)
  Creates an empty map content block that contains no statements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildblock(_:)-5ewn9)*