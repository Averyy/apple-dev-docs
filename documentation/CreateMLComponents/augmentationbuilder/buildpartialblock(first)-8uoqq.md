# buildPartialBlock(first:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

Builds a partial result from the first transformer.

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
static func buildPartialBlock(first: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

**Other overloads**:

```swift
static func buildPartialBlock(first: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

## Parameters

- `first`: A transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder/buildpartialblock(first:)-8uoqq)*