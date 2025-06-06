# string(at:effectiveRange:endsWithSearchBoundary:)

**Framework**: AppKit  
**Kind**: method

Returns the found string that is created by conceptually mapping its content to a single string, which is composed of a concatenation of all its substrings.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func string(at characterIndex: Int, effectiveRange outRange: NSRangePointer, endsWithSearchBoundary outFlag: UnsafeMutablePointer<ObjCBool>) -> String
```

#### Return Value

Returns the found string.

#### Discussion

See [`NSTextFinder`](nstextfinder.md) for more information.

## Parameters

- `characterIndex`: The given character index the client should return.
- `outRange`: Returns, by reference, the “effective range” of that substring in the full conceptually concatenated string
- `outFlag`: Returns, by-reference, whether the substring ends with a “search boundary”, meaning that NSTextFinder should not attempt to find any matches that overlap this boundary.

## See Also

- [var string: String](nstextfinderclient/string.md)
  Allows the client to specify a single string for searching.
- [func stringLength() -> Int](nstextfinderclient/stringlength.md)
  Returns the full length of the conceptually concatenated string return by the `stringAtIndex:effectiveRange:endsWithSearchBoundary:` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/string(at:effectiverange:endswithsearchboundary:))*