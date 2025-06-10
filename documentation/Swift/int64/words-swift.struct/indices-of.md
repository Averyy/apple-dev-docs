# indices(of:)

**Framework**: Swift  
**Kind**: method

Returns the indices of all the elements that are equal to the given element.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func indices(of element: Self.Element) -> RangeSet<Self.Index>
```

#### Return Value

A set of the indices of the elements that are equal to `element`.

#### Discussion

For example, you can use this method to find all the places that a particular letter occurs in a string.

```swift
let str = "Fresh cheese in a breeze"
let allTheEs = str.indices(of: "e")
// str[allTheEs].count == 7
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `element`: An element to look for in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int64/words-swift.struct/indices(of:))*