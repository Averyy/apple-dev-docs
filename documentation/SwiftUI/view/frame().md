# frame()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Positions this view within an invisible frame.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

> **Deprecated**: Use [`frame(width:height:alignment:)`](./frame%28width,height,alignment%29.md) or [`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`](./frame%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight,alignment%29.md) instead.

## Declaration

```swift
nonisolated
func frame() -> some View
```

## See Also

### Layout modifiers
- [func edgesIgnoringSafeArea(Edge.Set) -> some View](./edgesignoringsafearea%28_%29.md)
  Changes the view’s proposed area to extend outside the screen’s safe areas.
- [func coordinateSpace<T>(name: T) -> some View](./coordinatespace%28name%29.md)
  Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/frame())*