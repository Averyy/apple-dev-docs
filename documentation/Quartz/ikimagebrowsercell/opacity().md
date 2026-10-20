# opacity()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the opacity of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func opacity() -> CGFloat
```

```objc
- (CGFloat) opacity;
```

#### Return Value

The cell’s opacity.

#### Discussion

Possible values are between 0.0 (transparent) and 1.0 (opaque).

Subclasses can override this method to customize the opacity of the cell.

## See Also

### Cell Content Display
- [func imageAlignment() -> NSImageAlignment](./imagealignment%28%29.md)
  Returns the position of the cell’s image in the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/opacity())*