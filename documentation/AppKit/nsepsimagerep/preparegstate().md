# prepareGState()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implemented by subclasses to configure the graphics state prior to drawing.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
func prepareGState()
```

```objc
- (void) prepareGState;
```

## Discussion

The [`draw()`](../nsimagerep/draw%28%29.md) method of [`NSEPSImageRep`](../nsepsimagerep.md) sends this message to itself just before rendering the EPS code. The default implementation of this method does nothing. You can override it in your subclass to prepare the graphics state as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsepsimagerep/preparegstate())*