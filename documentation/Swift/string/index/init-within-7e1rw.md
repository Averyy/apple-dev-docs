# init(_:within:)

**Framework**: Swift  
**Kind**: init

Creates an index in the given Unicode scalars view that corresponds exactly to the specified `UTF16View` position.

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
init?(_ sourcePosition: String.Index, within unicodeScalars: String.UnicodeScalarView)
```

#### Discussion

The following example finds the position of a space in a string’s `utf16` view and then converts that position to an index in the string’s `unicodeScalars` view:

```swift
let cafe = "Café 🍵"

let utf16Index = cafe.utf16.firstIndex(of: 32)!
let scalarIndex = String.Index(utf16Index, within: cafe.unicodeScalars)!

print(String(cafe.unicodeScalars[..<scalarIndex]))
// Prints "Café"
```

If the index passed as `sourcePosition` doesn’t have an exact corresponding position in `unicodeScalars`, the result of the initializer is `nil`. For example, an attempt to convert the position of the trailing surrogate of a UTF-16 surrogate pair results in `nil`.

## Parameters

- `sourcePosition`: A position in the   view of a string.    must be an element of   .
- `unicodeScalars`: The   in which to find the new   position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index/init(_:within:)-7e1rw)*