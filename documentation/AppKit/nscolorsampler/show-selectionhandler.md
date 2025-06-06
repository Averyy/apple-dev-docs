# show(selectionHandler:)

**Framework**: AppKit  
**Kind**: method

Displays the system color-sampling interface asynchronously and reports the selected color back to your app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func sample() async -> NSColor?
```

#### Discussion

This method displays the color-sampling interface and returns immediately. The color-sampling interface magnifies the onscreen pixels and makes it easier for the user to select a single pixel. When the user clicks any mouse button, AppKit dismisses the interface and calls `selectionHandler` with the results.

## Parameters

- `selectionHandler`: The handler block for processing the user-selected color. AppKit calls this block on your app’s main thread. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorsampler/show(selectionhandler:))*