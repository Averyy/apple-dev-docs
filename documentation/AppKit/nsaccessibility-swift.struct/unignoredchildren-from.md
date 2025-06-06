# unignoredChildren(from:)

**Framework**: AppKit  
**Kind**: method

Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.

**Availability**:
- macOS ?+

## Declaration

```swift
static func unignoredChildren(from originalChildren: [Any]) -> [Any]
```

#### Discussion

This function first tests whether `originalChildren` contains any ignored objects. If the array contains no ignored objects, the function returns `originalChildren`. If the array contains ignored objects, this function returns a new array that contains the contents of `originalChildren`, but with each ignored object replaced by its unignored descendant.

## See Also

- [static func unignoredAncestor(of: Any) -> Any?](nsaccessibility-swift.struct/unignoredancestor(of:).md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](nsaccessibility-swift.struct/unignoredchildrenforonlychild(from:).md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](nsaccessibility-swift.struct/unignoreddescendant(of:).md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredchildren(from:))*