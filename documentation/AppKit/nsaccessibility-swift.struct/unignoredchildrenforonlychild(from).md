# unignoredChildrenForOnlyChild(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.

**Availability**:
- macOS

## Declaration

```swift
static func unignoredChildrenForOnlyChild(from originalChild: Any) -> [Any]
```

```c
extern NSArray *NSAccessibilityUnignoredChildrenForOnlyChild(id originalChild);
```

## Discussion

Tests whether `originalChild` is an ignored object and returns an array containing either `originalChild`, if it is not ignored, or its unignored descendants.

## See Also

### Getting Accessibility Objects
- [static func unignoredAncestor(of: Any) -> Any?](./unignoredancestor%28of%29.md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildren(from: [Any]) -> [Any]](./unignoredchildren%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](./unignoreddescendant%28of%29.md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:))*