# elementCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The total number of path elements in the path.

**Availability**:
- macOS

## Declaration

```swift
var elementCount: Int { get }
```

```objc
@property (readonly) NSInteger elementCount;
```

## Discussion

Each element type corresponds to one of the operations described in Path Elements.

## See Also

### Accessing Elements of a Path
- [var cgPath: CGPath](./cgpath.md)
- [func element(at: Int) -> NSBezierPath.ElementType](./element%28at%29.md)
  Returns the type of path element at the specified index.
- [func element(at: Int, associatedPoints: NSPointArray?) -> NSBezierPath.ElementType](./element%28at,associatedpoints%29.md)
  Gets the element type and (and optionally) the associated points for the path element at the specified index.
- [func removeAllPoints()](./removeallpoints%28%29.md)
  Removes all path elements from the path, effectively clearing the path.
- [func setAssociatedPoints(NSPointArray?, at: Int)](./setassociatedpoints%28_,at%29.md)
  Changes the points associated with the specified path element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/elementcount)*