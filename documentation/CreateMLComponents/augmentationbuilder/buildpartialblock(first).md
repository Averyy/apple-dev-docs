# buildPartialBlock(first:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

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

**Other overloads**:

```swift
static func buildPartialBlock(first: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

## Parameters

- `first`: A random transformer.

## See Also

### Building augmentations
- [static buildPartialBlock(accumulated:next:)](./buildpartialblock%28accumulated,next%29.md)
  Builds a partial result by combining an accumulated random transformer and a new random transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder/buildpartialblock(first:))*