# setMode(_:)

**Framework**: AppKit  
**Kind**: method

Overriden to set the color picker’s mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setMode(_ mode: NSColorPanel.Mode)
```

#### Discussion

In grayscale-alpha, red-green-blue, cyan-magenta-yellow-black, and hue-saturation-brightness modes, the user adjusts colors by manipulating sliders. In the custom palette mode, the user can load an `NSImage` file (TIFF or EPS) into the `NSColorPanel`, then select colors from the image. In custom color list mode, the user can create and load lists of named colors. The two custom modes provide `NSPopUpList`s for loading and saving files. Finally, color wheel mode provides a simplified control for selecting colors.

## Parameters

- `mode`: A constant specifying the color picking mode. These constants are defined in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker/setmode(_:))*