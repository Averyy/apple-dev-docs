# unignoredAncestor(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an unignored accessibility object, ascending the hierarchy, if necessary.

**Availability**:
- macOS

## Declaration

```swift
static func unignoredAncestor(of element: Any) -> Any?
```

```c
extern idNSAccessibilityUnignoredAncestor(id element);
```

#### Discussion

Tests whether `element` is an ignored object, returning either `element`, if it is not ignored, or the first unignored ancestor of `element`.

## See Also

### Getting Accessibility Objects
- [static func unignoredChildren(from: [Any]) -> [Any]](./unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](./unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](./unignoreddescendant%28of%29.md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredancestor(of:))*