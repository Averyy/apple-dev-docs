# unignoredAncestor(of:)

**Framework**: AppKit  
**Kind**: method

Returns an unignored accessibility object, ascending the hierarchy, if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
static func unignoredAncestor(of element: Any) -> Any?
```

#### Discussion

Tests whether `element` is an ignored object, returning either `element`, if it is not ignored, or the first unignored ancestor of `element`.

## See Also

- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](nsaccessibility-swift.struct/unignoreddescendant(of:).md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredancestor(of:))*