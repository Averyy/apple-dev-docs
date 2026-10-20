# shuffled(using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<id> *) shuffledArrayWithRandomSource:(GKRandomSource *) randomSource;
```

#### Return Value

A new array that lists this array’s elements in a random order.

#### Discussion

Use the `randomSource` parameter to influence the random shuffling. For example, to reproduce a series of shuffles for testing, you can create a [`GKARC4RandomSource`](../../GameplayKit/gkarc4randomsource.md) object using the [`seed`](../../GameplayKit/gkarc4randomsource/seed.md) value of a previously used random source.

This method is equivalent to the [`GKRandomSource`](../../GameplayKit/gkrandomsource.md) method [`arrayByShufflingObjects(in:)`](../../GameplayKit/gkrandomsource/arraybyshufflingobjects%28in%29.md), but as an [`NSArray`](../nsarray.md) method it preserves generic type parameters.

## Parameters

- `randomSource`: A GameplayKit random source object.

## See Also

### Randomly Shuffling an Array
- [func shuffled() -> [Any]](./shuffled%28%29.md)
  Returns a new array that lists this array’s elements in a random order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/shuffled(using:))*