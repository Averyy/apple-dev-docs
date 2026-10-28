# buildPartialBlock(accumulated:next:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

Builds a partial result by combining an accumulated random transformer and a new transformer.

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
static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some Transformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

**Other overloads**:

```swift
static func buildPartialBlock(accumulated: some RandomTransformer<Element, Element>, next: some RandomTransformer<Element, Element>) -> some RandomTransformer<Element, Element>
```

## Parameters

- `accumulated`: A random transformer representing the accumulated result thus far.
- `next`: A transformer representing the next component after the accumulated ones in the block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder/buildpartialblock(accumulated:next:)-4a0qn)*