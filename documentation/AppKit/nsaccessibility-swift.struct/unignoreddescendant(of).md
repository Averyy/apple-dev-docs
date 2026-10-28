# unignoredDescendant(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an unignored accessibility object, descending the hierarchy, if necessary.

**Availability**:
- macOS

## Declaration

```swift
static func unignoredDescendant(of element: Any) -> Any?
```

```c
extern idNSAccessibilityUnignoredDescendant(id element);
```

## Discussion

Tests whether `element` is an ignored object, returning either `element`, if it is not ignored, or the first unignored descendant of `element`. Use this function only if you know there is a linear, one-to-one, hierarchy below `element`. Otherwise, if `element` has either no unignored children or multiple unignored children, this function fails and returns `nil`.

## See Also

### Getting Accessibility Objects
- [static func unignoredAncestor(of: Any) -> Any?](./unignoredancestor%28of%29.md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](./unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](./unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoreddescendant(of:))*