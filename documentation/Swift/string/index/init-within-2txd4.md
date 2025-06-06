# init(_:within:)

**Framework**: Swift  
**Kind**: init

Creates an index in the given UTF-16 view that corresponds exactly to the specified string position.

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
init?(_ idx: String.Index, within target: String.UTF16View)
```

#### Discussion

If the index passed as `sourcePosition` represents either the start of a Unicode scalar value or the position of a UTF-16 trailing surrogate, then the initializer succeeds. If `sourcePosition` does not have an exact corresponding position in `target`, then the result is `nil`. For example, an attempt to convert the position of a UTF-8 continuation byte results in `nil`.

The following example finds the position of a space in a string and then converts that position to an index in the string’s `utf16` view.

```swift
let cafe = "Café 🍵"

let stringIndex = cafe.firstIndex(of: "é")!
let utf16Index = String.Index(stringIndex, within: cafe.utf16)!

print(String(cafe.utf16[...utf16Index])!)
// Prints "Café"
```

## Parameters

- `idx`: A position in at least one of the views of the string   shared by  .
- `target`: The   in which to find the new position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index/init(_:within:)-2txd4)*