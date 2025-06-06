# unignoredDescendant(of:)

**Framework**: AppKit  
**Kind**: method

Returns an unignored accessibility object, descending the hierarchy, if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
static func unignoredDescendant(of element: Any) -> Any?
```

#### Discussion

Tests whether `element` is an ignored object, returning either `element`, if it is not ignored, or the first unignored descendant of `element`. Use this function only if you know there is a linear, one-to-one, hierarchy below `element`. Otherwise, if `element` has either no unignored children or multiple unignored children, this function fails and returns `nil`.

## See Also

- [static func unignoredAncestor(of: Any) -> Any?](nsaccessibility-swift.struct/unignoredancestor(of:).md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoreddescendant(of:))*