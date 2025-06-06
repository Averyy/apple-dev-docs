# isTrailSurrogate(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the specified code unit is a low-surrogate code unit.

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
static func isTrailSurrogate(_ x: Unicode.UTF16.CodeUnit) -> Bool
```

#### Return Value

`true` if `x` is a low-surrogate code unit; otherwise, `false`.

#### Discussion

Here’s an example of checking whether each code unit in a string’s `utf16` view is a trailing surrogate. The `apple` string contains a single emoji character made up of a surrogate pair when encoded in UTF-16.

```swift
let apple = "🍎"
for unit in apple.utf16 {
    print(UTF16.isTrailSurrogate(unit))
}
// Prints "false"
// Prints "true"
```

This method does not validate the encoding of a UTF-16 sequence beyond the specified code unit. Specifically, it does not validate that a high-surrogate code unit precedes `x`.

## Parameters

- `x`: A UTF-16 code unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf16/istrailsurrogate(_:))*