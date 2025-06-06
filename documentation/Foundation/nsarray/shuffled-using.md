# shuffled(using:)

**Framework**: Foundation  
**Kind**: method

Returns a new array that lists this array’s elements in a random order, using the specified random source.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shuffled(using randomSource: GKRandomSource) -> [Any]
```

#### Return Value

A new array that lists this array’s elements in a random order.

#### Discussion

Use the `randomSource` parameter to influence the random shuffling. For example, to reproduce a series of shuffles for testing, you can create a [`GKARC4RandomSource`](https://developer.apple.com/documentation/GameplayKit/GKARC4RandomSource) object using the [`seed`](https://developer.apple.com/documentation/GameplayKit/GKARC4RandomSource/seed) value of a previously used random source.

This method is equivalent to the [`GKRandomSource`](https://developer.apple.com/documentation/GameplayKit/GKRandomSource) method [`arrayByShufflingObjects(in:)`](https://developer.apple.com/documentation/GameplayKit/GKRandomSource/arrayByShufflingObjects(in:)), but as an [`NSArray`](nsarray.md) method it preserves generic type parameters.

## Parameters

- `randomSource`: A GameplayKit random source object.

## See Also

- [func shuffled() -> [Any]](nsarray/shuffled.md)
  Returns a new array that lists this array’s elements in a random order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/shuffled(using:))*