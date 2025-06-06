# rangeContainerObject

**Framework**: Foundation  
**Kind**: property

Sets the top-level container object for a range-specifier evaluation to a give object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var rangeContainerObject: Any? { get set }
```

#### Discussion

Instances of `NSRangeSpecifier` contain object specifiers representing the first or last element in a range of elements, and these specifiers are evaluated in the context of `container`.

## Parameters

- `container`: The top-level container object for a range-specifier evaluation.

## See Also

- [var topLevelObject: Any?](nsscriptexecutioncontext/toplevelobject.md)
  Sets the top-level object for an object-specifier evaluation.
- [var objectBeingTested: Any?](nsscriptexecutioncontext/objectbeingtested.md)
  Sets the top-level container object currently being tested in a “whose” qualifier to a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/rangecontainerobject)*