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
subscript(r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView.SubSequence { get }
```

#### Overview

The accessed slice uses the same indices for the same elements as the original collection uses. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```swift
let streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let index = streetsSlice.firstIndex(of: "Evarts")    // 4
print(streets[index!])
// Prints "Evarts"
```

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/subscript(_:)-6aml8)*