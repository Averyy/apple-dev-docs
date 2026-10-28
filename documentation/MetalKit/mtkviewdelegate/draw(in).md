# draw(in:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws the view’s contents.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func draw(in view: MTKView)
```

```objc
- (void) drawInMTKView:(MTKView *) view;
```

## Discussion

This method is called on the delegate when it is asked to render into the view.

## Parameters

- `view`: The view requesting that its contents be redrawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkviewdelegate/draw(in:))*