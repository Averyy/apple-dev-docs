# unignoredChildren(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.

**Availability**:
- macOS

## Declaration

```swift
static func unignoredChildren(from originalChildren: [Any]) -> [Any]
```

```c
extern NSArray *NSAccessibilityUnignoredChildren(NSArray *originalChildren);
```

## Discussion

This function first tests whether `originalChildren` contains any ignored objects. If the array contains no ignored objects, the function returns `originalChildren`. If the array contains ignored objects, this function returns a new array that contains the contents of `originalChildren`, but with each ignored object replaced by its unignored descendant.

## See Also

### Getting Accessibility Objects
- [static func unignoredAncestor(of: Any) -> Any?](./unignoredancestor%28of%29.md)
  Returns an unignored accessibility object, ascending the hierarchy, if necessary.
- [static func unignoredChildrenForOnlyChild(from: Any) -> [Any]](./unignoredchildrenforonlychild%28from%29.md)
  Returns a list of unignored accessibility objects, descending the hierarchy, if necessary.
- [static func unignoredDescendant(of: Any) -> Any?](./unignoreddescendant%28of%29.md)
  Returns an unignored accessibility object, descending the hierarchy, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/unignoredchildren(from:))*