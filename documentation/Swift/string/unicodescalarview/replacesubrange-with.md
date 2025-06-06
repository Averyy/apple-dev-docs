# replaceSubrange(_:with:)

**Framework**: Swift  
**Kind**: method

Replaces the elements within the specified bounds with the given Unicode scalar values.

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
mutating func replaceSubrange<C>(_ subrange: Range<String.UnicodeScalarView.Index>, with newElements: C) where C : Collection, C.Element == Unicode.Scalar
```

#### Discussion

Calling this method invalidates any existing indices for use with this string.

> **Note**: O(), where  is the combined length of the view and `newElements`. If the call to `replaceSubrange(_:with:)` simply removes elements at the end of the string, the complexity is O(), where  is equal to `bounds.count`.

O(), where  is the combined length of the view and `newElements`. If the call to `replaceSubrange(_:with:)` simply removes elements at the end of the string, the complexity is O(), where  is equal to `bounds.count`.

## Parameters

- `subrange`: The range of elements to replace. The bounds of the range   must be valid indices of the view.
- `newElements`: The new Unicode scalar values to add to the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/replacesubrange(_:with:))*