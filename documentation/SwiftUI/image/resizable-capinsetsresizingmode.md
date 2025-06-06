# resizable(capInsets:resizingMode:)

**Framework**: SwiftUI  
**Kind**: method

Sets the mode by which SwiftUI resizes an image to fit its space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func resizable(capInsets: EdgeInsets = EdgeInsets(), resizingMode: Image.ResizingMode = .stretch) -> Image
```

## Mentions

- [Fitting images into available space](fitting-images-into-available-space.md)

#### Return Value

An image, with the new resizing behavior set.

## Parameters

- `capInsets`: Inset values that indicate a portion of the image that   SwiftUI doesn’t resize.
- `resizingMode`: The mode by which SwiftUI resizes the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/resizable(capinsets:resizingmode:))*