# replaceSubrange(_:with:)

**Framework**: Swift  
**Kind**: method

Replaces the text within the specified bounds with the given characters.

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
mutating func replaceSubrange<C>(_ subrange: Range<String.Index>, with newElements: C) where C : Collection, C.Element == Character
```

#### Discussion

Calling this method invalidates any existing indices for use with this string.

> **Note**: O(), where  is the combined length of the string and `newElements`. If the call to `replaceSubrange(_:with:)` simply removes text at the end of the string, the complexity is O(), where  is equal to `bounds.count`.

## Parameters

- `subrange`: The range of text to replace. The bounds of the range must be   valid indices of the string.
- `newElements`: The new characters to add to the string.

## See Also

- [func replaceSubrange<C, R>(R, with: C)](string/replacesubrange(_:with:)-72947.md)
  Replaces the specified subrange of elements with the given collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/replacesubrange(_:with:))*