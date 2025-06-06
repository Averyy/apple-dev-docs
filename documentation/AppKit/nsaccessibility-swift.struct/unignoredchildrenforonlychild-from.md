# unignoredChildrenForOnlyChild(from:)

**Framework**: AppKit  
**Kind**: method

Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
static func unignoredChildrenForOnlyChild(from originalChild: Any) -> [Any]
```

#### Discussion

Tests whether `originalChild` is an ignored object and returns an array containing either `originalChild`, if it is not ignored, or its unignored descendants.

## See Also

- [static func unignoredAncestor(of: Any) -> Any?](nsaccessibility-swift.struct/unignoredancestor(of:).md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](nsaccessibility-swift.struct/unignoredchildren(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](nsaccessibility-swift.struct/unignoreddescendant(of:).md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:))*