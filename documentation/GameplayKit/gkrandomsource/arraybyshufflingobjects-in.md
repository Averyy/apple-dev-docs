# arrayByShufflingObjects(in:)

**Framework**: GameplayKit  
**Kind**: method

Returns an array whose contents are the same as those of the specified array, but in a random order determined by the random source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func arrayByShufflingObjects(in array: [Any]) -> [Any]
```

#### Return Value

An array whose contents have been randomly shuffled.

#### Discussion

Use this method with an instance of [`GKRandomSource`](gkrandomsource.md) (or of one of its subclasses) to randomly rearrange the contents of an array. For example, in a card game you might use this method to randomize an array of card objects.

## Parameters

- `array`: An array of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomsource/arraybyshufflingobjects(in:))*