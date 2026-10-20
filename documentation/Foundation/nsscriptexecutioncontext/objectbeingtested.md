# objectBeingTested

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the top-level container object currently being tested in a “whose” qualifier to a given object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var objectBeingTested: Any? { get set }
```

```objc
@property (retain, nullable) id objectBeingTested;
```

## Parameters

- `object`: The top-level container object currently being tested.

## See Also

### Getting and setting the container object
- [var topLevelObject: Any?](./toplevelobject.md)
  Sets the top-level object for an object-specifier evaluation.
- [var rangeContainerObject: Any?](./rangecontainerobject.md)
  Sets the top-level container object for a range-specifier evaluation to a give object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/objectbeingtested)*