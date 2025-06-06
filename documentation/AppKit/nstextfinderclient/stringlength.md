# stringLength()

**Framework**: AppKit  
**Kind**: method

Returns the full length of the conceptually concatenated string return by the `stringAtIndex:effectiveRange:endsWithSearchBoundary:` method.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func stringLength() -> Int
```

#### Return Value

Returns the full length of the conceptually concatenated string in the second model, that is, the sum of the lengths of all of its substrings.

#### Discussion

See [`NSTextFinder`](nstextfinder.md) for more information.

## See Also

- [var string: String](nstextfinderclient/string.md)
  Allows the client to specify a single string for searching.
- [func string(at: Int, effectiveRange: NSRangePointer, endsWithSearchBoundary: UnsafeMutablePointer<ObjCBool>) -> String](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md)
  Returns the found string that is created by conceptually mapping its content to a single string, which is composed of a concatenation of all its substrings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/stringlength())*