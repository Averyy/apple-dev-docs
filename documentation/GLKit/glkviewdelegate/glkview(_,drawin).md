# glkView(_:drawIn:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws the view’s contents.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func glkView(_ view: GLKView, drawIn rect: CGRect)
```

```objc
- (void) glkView:(GLKView *) view drawInRect:(CGRect) rect;
```

## Discussion

The semantics of this method are identical to those of the [`draw(_:)`](../../UIKit/uiview/draw%28_%29.md) method; the [`GLKView`](../glkview.md) object makes its OpenGL ES context the current context and binds its framebuffer as the target for OpenGL ES rendering commands. Your delegate method should then draw the view’s contents.

## Parameters

- `view`: The view requesting that its contents be redrawn.
- `rect`: A rectangle that describes the area that needs to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewdelegate/glkview(_:drawin:))*