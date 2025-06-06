# mediaLibraries

**Framework**: AppKit  
**Kind**: property

The media library that is in use.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var mediaLibraries: NSMediaLibraryBrowserController.Library { get set }
```

#### Discussion

This property will be one of the values in the [`NSMediaLibraryBrowserController.Library`](nsmedialibrarybrowsercontroller/library.md) constants.

You can set the value to use a specific library (image, audio or movie). You can also read the value to determine which is currently displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/medialibraries)*