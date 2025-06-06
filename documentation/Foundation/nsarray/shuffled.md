# shuffled()

**Framework**: Foundation  
**Kind**: method

Returns a new array that lists this array’s elements in a random order.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shuffled() -> [Any]
```

#### Return Value

A new array that lists this array’s elements in a random order.

#### Discussion

Calling this method is equivalent to calling the [`shuffled(using:)`](nsarray/shuffled(using:).md) method and passing the system [`sharedRandom()`](https://developer.apple.com/documentation/GameplayKit/GKRandomSource/sharedRandom()) random source. To influence the random shuffling or to be able to deterministically reproduce a series of shuffles, create your own [`GKRandomSource`](https://developer.apple.com/documentation/GameplayKit/GKRandomSource) object.

## See Also

- [func shuffled(using: GKRandomSource) -> [Any]](nsarray/shuffled(using:).md)
  Returns a new array that lists this array’s elements in a random order, using the specified random source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/shuffled())*