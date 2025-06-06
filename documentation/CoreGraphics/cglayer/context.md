# context

**Framework**: Core Graphics  
**Kind**: property

Returns the graphics context associated with a layer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var context: CGContext? { get }
```

#### Discussion

The context that’s returned is the context for the layer itself, not the context that you specified when you created the layer.

## See Also

- [var size: CGSize](cglayer/size.md)
  Returns the width and height of a layer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayer/context)*