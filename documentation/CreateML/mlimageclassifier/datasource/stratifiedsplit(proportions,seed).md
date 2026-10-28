# stratifiedSplit(proportions:seed:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates an array of labeled image dictionaries by splitting the data source into strata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed()) throws -> [[String : [URL]]]
```

## Return Value

An array of dictionaries of labeled images.

## Parameters

- `proportions`: An array of proportions, each in the range `[0.0, 1.0]`.
- `seed`: A seed number for the random-number generator.

## See Also

### Splitting the data
- [func stratifiedSplit<RNG>(proportions: [Double], generator: inout RNG) throws -> [[String : [URL]]]](./stratifiedsplit%28proportions,generator%29.md)
  Generates an array of labeled image dictionaries by splitting the data source into strata using the random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/datasource/stratifiedsplit(proportions:seed:))*