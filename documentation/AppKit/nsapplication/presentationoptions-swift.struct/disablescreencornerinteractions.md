# disableScreenCornerInteractions

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Disable screen corner interactions when the application is frontmost.

**Availability**:
- macOS 27.0+

## Declaration

```swift
static var disableScreenCornerInteractions: NSApplication.PresentationOptions { get }
```

```c
NSApplicationPresentationDisableScreenCornerInteractions
```

#### Discussion

`.autoHideDock` or `.hideDock` must also be set for this option to take effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct/disablescreencornerinteractions)*