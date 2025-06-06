# accessibilityBrailleMapRenderRegion

**Framework**: Accessibility  
**Kind**: property

A region of the UI that the system converts into a braille map and displays on the braille display.

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
optional var accessibilityBrailleMapRenderRegion: CGRect { get set }
```

#### Discussion

When the accessibility element that implements this property has focus, the system uses this value to update the braille display automatically.

Set this value to specify a region of the accessibility element — relative to its bounds — to display on the braille display. VoiceOver snapshots the region of the accessibility element that you specify, converts the data to a braille map, and renders the braille map to the braille display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axbraillemaprenderer/accessibilitybraillemaprenderregion)*