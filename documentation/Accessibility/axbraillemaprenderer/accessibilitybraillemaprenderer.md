# accessibilityBrailleMapRenderer

**Framework**: Accessibility  
**Kind**: property

A handler that the system calls to let you update the Braille map.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.1+
- tvOS 15.2+
- visionOS 1.0+
- watchOS 8.2+

## Declaration

```swift
optional var accessibilityBrailleMapRenderer: (AXBrailleMap) -> Void { get set }
```

#### Discussion

When the accessibility element that implements this property has focus, the system calls this handler to let you update the braille map manually.

Use this handler to modify the braille map that the system passes in with the new data you want to display. The following code shows a basic implementation of [`accessibilityBrailleMapRenderer`](axbraillemaprenderer/accessibilitybraillemaprenderer.md):

```swift
self.accessibilityBrailleMapRenderer = { map in

    // Get the data to render to the braille display.
    guard let image = self.myImageView.image?.cgImage else { return }

    // Update the braille map with the data.
    map.present(image)
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemaprenderer/accessibilitybraillemaprenderer)*