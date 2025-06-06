# randomSplit(by:seed:)

**Framework**: Create ML Components  
**Kind**: method

Generates two generic arrays by randomly splitting the elements of the sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func randomSplit<T>(by proportion: Double, seed: Int? = nil) -> (ArraySlice<T>, ArraySlice<T>) where T == Self.Element
```

#### Return Value

A tuple of array slices.

## Parameters

- `proportion`: A proportion in the range  .
- `seed`: A seed number for a random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/randomsplit(by:seed:)-9skcq)*