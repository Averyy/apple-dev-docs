# stratifiedSplit(proportions:generator:)

**Framework**: Create ML  
**Kind**: method

Generates an array of labeled audio dictionaries by splitting the data source into strata using the random-number generator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]] where RNG : RandomNumberGenerator
```

#### Return Value

An array of dictionaries of labeled audio files. Each dictionary key is a label string and its value is an array of audio-file URLs.

## Parameters

- `proportions`: An array of proportions, each in the range  .
- `generator`: A random-number generator.

## See Also

- [func stratifiedSplit(proportions: [Double], seed: Int) throws -> [[String : [URL]]]](mlsoundclassifier/datasource/stratifiedsplit(proportions:seed:).md)
  Generates an array of labeled audio dictionaries by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/datasource/stratifiedsplit(proportions:generator:))*