# topLevelObject

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the top-level object for an object-specifier evaluation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var topLevelObject: Any? { get set }
```

```objc
@property (retain, nullable) id topLevelObject;
```

## Parameters

- `anObject`: The top-level object for an object-specifier evaluation.

## See Also

### Getting and setting the container object
- [var objectBeingTested: Any?](./objectbeingtested.md)
  Sets the top-level container object currently being tested in a “whose” qualifier to a given object.
- [var rangeContainerObject: Any?](./rangecontainerobject.md)
  Sets the top-level container object for a range-specifier evaluation to a give object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/toplevelobject)*