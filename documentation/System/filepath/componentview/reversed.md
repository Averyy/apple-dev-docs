# reversed()

**Framework**: System  
**Kind**: method

Returns a view presenting the elements of the collection in reverse order.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func reversed() -> ReversedCollection<Self>
```

#### Discussion

You can reverse a collection without allocating new space for its elements by calling this `reversed()` method. A `ReversedCollection` instance wraps an underlying collection and provides access to its elements in reverse order. This example prints the characters of a string in reverse order:

```swift
let word = "Backwards"
for char in word.reversed() {
    print(char, terminator: "")
}
// Prints "sdrawkcaB"
```

If you need a reversed collection of the same type, you may be able to use the collection’s sequence-based or collection-based initializer. For example, to get the reversed version of a string, reverse its characters and initialize a new `String` instance from the result.

```swift
let reversedWord = String(word.reversed())
print(reversedWord)
// Prints "sdrawkcaB"
```

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/reversed())*