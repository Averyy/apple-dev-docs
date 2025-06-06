# buildPartialBlock(accumulated:next:)

**Framework**: Swift Charts  
**Kind**: method

Builds a partial result by combining an accumulated component and a new component.

## Declaration

```swift
static func buildPartialBlock(accumulated: some ChartContent, next: some ChartContent) -> some ChartContent
```

## Parameters

- `accumulated`: The accumulated result.
- `next`: The next component to accumulate.

## See Also

- [static func buildPartialBlock<T>(first: T) -> T](chartcontentbuilder/buildpartialblock(first:).md)
  Builds a partial result from a single, first component.
- [static func buildBlock() -> some ChartContent](chartcontentbuilder/buildblock.md)
  Produces empty chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontentbuilder/buildpartialblock(accumulated:next:))*