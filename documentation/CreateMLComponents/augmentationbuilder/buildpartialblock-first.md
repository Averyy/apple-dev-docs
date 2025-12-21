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

- [static buildPartialBlock(accumulated:next:)](augmentationbuilder/buildpartialblock(accumulated:next:).md)
  Builds a partial result by combining an accumulated random transformer and a new random transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder/buildpartialblock(first:))*