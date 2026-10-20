# setClip()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the clipping path of the current graphics context with the area inside the path.

**Availability**:
- macOS

## Declaration

```swift
func setClip()
```

```objc
- (void) setClip;
```

#### Discussion

You should avoid using this method as a way of adjusting the clipping path, as it may expand the clipping path beyond the bounds set by the enclosing view. If you do use this method, be sure to save the graphics state prior to modifying the clipping path and restore the graphics state when you are done.

This method uses the current winding rule to determine the clipping shape of the receiver. This method does not affect the receiver’s path.

## See Also

### Related Documentation
- [func saveGraphicsState()](../nsgraphicscontext/savegraphicsstate%28%29-swift.method.md)
  Saves the current graphics state and creates a new graphics state on the top of the stack.
- [func restoreGraphicsState()](../nsgraphicscontext/restoregraphicsstate%28%29-swift.method.md)
  Removes the context’s graphics state from the top of the graphics state stack and makes the next graphics state the current graphics state.
### Specifying a Clipping Path
- [func addClip()](./addclip%28%29.md)
  Intersects the area enclosed by the path with the clipping path of the current graphics context and makes the resulting shape the current clipping path.
- [class func clip(NSRect)](./clip%28_%29.md)
  Intersects the specified rectangle with the clipping path of the current graphics context and makes the resulting shape the current clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/setclip())*