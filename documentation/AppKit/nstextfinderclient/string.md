# string

**Framework**: AppKit  
**Kind**: property

Allows the client to specify a single string for searching.

**Availability**:
- macOS ?+

## Declaration

```swift
optional var string: String { get }
```

#### Discussion

If the client cannot logically or efficiently flatten itself into a single string, then the [`string(at:effectiveRange:endsWithSearchBoundary:)`](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md) and [`stringLength()`](nstextfinderclient/stringlength().md) methods should be implemented instead.

## See Also

- [func string(at: Int, effectiveRange: NSRangePointer, endsWithSearchBoundary: UnsafeMutablePointer<ObjCBool>) -> String](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md)
  Returns the found string that is created by conceptually mapping its content to a single string, which is composed of a concatenation of all its substrings.
- [func stringLength() -> Int](nstextfinderclient/stringlength.md)
  Returns the full length of the conceptually concatenated string return by the `stringAtIndex:effectiveRange:endsWithSearchBoundary:` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/string)*