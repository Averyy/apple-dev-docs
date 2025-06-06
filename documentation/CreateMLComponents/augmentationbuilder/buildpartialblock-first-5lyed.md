# buildPartialBlock(first:)

**Framework**: Create ML Components  
**Kind**: method

Builds a partial result random transformer from the first random transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
static func buildPartialBlock(first: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

## Parameters

- `first`: A random transformer.

## See Also

- [static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(accumulated:next:)-3h3fp.md)
  Builds a partial result by combining an accumulated random transformer and a new random transformer.
- [static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(accumulated:next:)-4a0qn.md)
  Builds a partial result by combining an accumulated random transformer and a new transformer.
- [static func buildPartialBlock(first: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
](augmentationbuilder/buildpartialblock(first:)-8uoqq.md)
  Builds a partial result from the first transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder/buildpartialblock(first:)-5lyed)*