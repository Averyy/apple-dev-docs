# element(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the type of path element at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func element(at index: Int) -> NSBezierPath.ElementType
```

```objc
- (NSBezierPathElement) elementAtIndex:(NSInteger) index;
```

#### Return Value

The type of the path element. For a list of constants, see [`NSBezierPath.ElementType`](./elementtype.md).

#### Discussion

Path elements describe the commands used to define a path and include basic commands such as moving to a specific point, creating a line segment, creating a curve, or closing the path. The elements are stored in the order of their execution.

## Parameters

- `index`: The index of the desired path element.

## See Also

### Related Documentation
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.
### Accessing Elements of a Path
- [var cgPath: CGPath](./cgpath.md)
- [var elementCount: Int](./elementcount.md)
  The total number of path elements in the path.
- [func element(at: Int, associatedPoints: NSPointArray?) -> NSBezierPath.ElementType](./element%28at,associatedpoints%29.md)
  Gets the element type and (and optionally) the associated points for the path element at the specified index.
- [func removeAllPoints()](./removeallpoints%28%29.md)
  Removes all path elements from the path, effectively clearing the path.
- [func setAssociatedPoints(NSPointArray?, at: Int)](./setassociatedpoints%28_,at%29.md)
  Changes the points associated with the specified path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/element(at:))*