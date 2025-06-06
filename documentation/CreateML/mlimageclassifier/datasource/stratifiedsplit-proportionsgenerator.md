# stratifiedSplit(proportions:generator:)

**Framework**: Create ML  
**Kind**: method

Generates an array of labeled image dictionaries by splitting the data source into strata using the random-number generator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]] where RNG : RandomNumberGenerator
```

#### Return Value

An array of dictionaries of labeled images.

## Parameters

- `proportions`: An array of proportions, each in the range  .
- `generator`: A random-number generator.

## See Also

- [func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]](mlimageclassifier/datasource/stratifiedsplit(proportions:seed:).md)
  Generates an array of labeled image dictionaries by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource/stratifiedsplit(proportions:generator:))*