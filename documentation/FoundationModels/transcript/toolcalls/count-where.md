# count(where:)

**Framework**: Foundation Models  
**Kind**: method

Returns the number of elements in the sequence that satisfy the given predicate.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func count<E>(where predicate: (Self.Element) throws(E) -> Bool) throws(E) -> Int where E : Error
```

#### Return Value

The number of elements in the sequence that satisfy the given predicate.

#### Discussion

You can use this method to count the number of elements that pass a test. The following example finds the number of names that are fewer than five characters long:

```None
let names = ["Jacqueline", "Ian", "Amy", "Juan", "Soroush", "Tiffany"]
let shortNameCount = names.count(where: { $0.count < 5 })
// shortNameCount == 3
```

To find the number of times a specific element appears in the sequence, use the equal to operator (`==`) in the closure to test for a match.

```None
let birds = ["duck", "duck", "duck", "duck", "goose"]
let duckCount = birds.count(where: { $0 == "duck" })
// duckCount == 4
```

The sequence must be finite.

## Parameters

- `predicate`: A closure that takes each element of the sequence   as its argument and returns a Boolean value indicating whether   the element should be included in the count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/count(where:))*