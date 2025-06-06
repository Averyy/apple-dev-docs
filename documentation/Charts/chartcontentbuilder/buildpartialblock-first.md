# buildPartialBlock(first:)

**Framework**: Swift Charts  
**Kind**: method

Builds a partial result from a single, first component.

## Declaration

```swift
static func buildPartialBlock<T>(first content: T) -> T where T : ChartContent
```

## Parameters

- `content`: The first component to accumulate.

## See Also

- [static func buildPartialBlock(accumulated: some ChartContent, next: some ChartContent) -> some ChartContent](chartcontentbuilder/buildpartialblock(accumulated:next:).md)
  Builds a partial result by combining an accumulated component and a new component.
- [static func buildBlock() -> some ChartContent](chartcontentbuilder/buildblock.md)
  Produces empty chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontentbuilder/buildpartialblock(first:))*