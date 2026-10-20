# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses a contiguous subrange of the collection’s elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 4.0+

## Declaration

```swift
subscript(r: Range<String.UTF8View.Index>) -> String.UTF8View.SubSequence { get }
```

#### Overview

For example, using a `PartialRangeFrom` range expression with an array accesses the subrange from the start of the range expression until the end of the array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2..<5]
print(streetsSlice)
// ["Channing", "Douglas", "Evarts"]
```

The accessed slice uses the same indices for the same elements as the original collection. This example searches `streetsSlice` for one of the strings in the slice, and then uses that index in the original array.

```swift
let index = streetsSlice.firstIndex(of: "Evarts")!    // 4
print(streets[index])
// "Evarts"
```

Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value. Attempting to access an element by using an index outside the bounds of the slice may result in a runtime error, even if that index is valid for the original collection.

```swift
print(streetsSlice.startIndex)
// 2
print(streetsSlice[2])
// "Channing"

print(streetsSlice[0])
// error: Index out of bounds
```

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf8view/subscript(_:)-3wo7k)*