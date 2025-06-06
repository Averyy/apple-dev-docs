# joined()

**Framework**: Swift  
**Kind**: method

Returns the elements of this sequence of sequences, concatenated.

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
func joined() -> FlattenSequence<Self>
```

#### Return Value

A flattened view of the elements of this sequence of sequences.

#### Discussion

In this example, an array of three ranges is flattened so that the elements of each range can be iterated in turn.

```swift
let ranges = [0..<3, 8..<10, 15..<17]

// A for-in loop over 'ranges' accesses each range:
for range in ranges {
  print(range)
}
// Prints "0..<3"
// Prints "8..<10"
// Prints "15..<17"

// Use 'joined()' to access each element of each range:
for index in ranges.joined() {
    print(index, terminator: " ")
}
// Prints: "0 1 2 8 9 15 16"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/joined())*