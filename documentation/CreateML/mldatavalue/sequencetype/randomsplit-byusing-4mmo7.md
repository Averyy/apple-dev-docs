# randomSplit(by:using:)

**Framework**: Create ML  
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
func randomSplit<T, Generator>(by proportion: Double, using generator: inout Generator) -> (ArraySlice<T>, ArraySlice<T>) where T == Self.Element, Generator : RandomNumberGenerator
```

#### Return Value

A tuple of array slices.

## Parameters

- `proportion`: A proportion in the range  .
- `generator`: A random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/sequencetype/randomsplit(by:using:)-4mmo7)*