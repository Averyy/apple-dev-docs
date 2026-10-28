# joined(separator:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func joined(separator: String = "") -> String
```

Available when `Element` conforms to `StringProtocol`.

## Return Value

A single, concatenated string.

## Discussion

The following example shows how an array of strings can be joined to a single, comma-separated string:

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let list = cast.joined(separator: ", ")
print(list)
// Prints "Vivien, Marlon, Kim, Karl"
```

## Parameters

- `separator`: A string to insert between each of the elements in this sequence. The default separator is an empty string.

## See Also

### Splitting and Joining Elements
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [ArraySlice<Self.Element>]](./split%28maxsplits,omittingemptysubsequences,whereseparator%29.md)
  Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [ArraySlice<Self.Element>]](./split%28separator,maxsplits,omittingemptysubsequences%29.md)
  Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [func joined() -> FlattenSequence<Self>](./joined%28%29.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](./joined%28separator%29-7w47r.md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/joined(separator:)-5zjyj)*