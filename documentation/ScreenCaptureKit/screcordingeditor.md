# SCRecordingEditor

**Framework**: ScreenCaptureKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class SCRecordingEditor
```

#### Overview

Presents a system-owned preview UI for a completed recording via SCStream.

SCRecordingEditor owns the full presentation lifecycle of the preview UI. Callers provide an optional anchor window (macOS) or scene; if none is provided, the foreground window/scene is discovered automatically.

## Topics

### Initializers
- [init(URL: URL)](screcordingeditor/init(url:)-1k2cv.md)
- [init(url: URL)](screcordingeditor/init(url:)-ead5.md)
### Instance Properties
- [var delegate: (any SCRecordingEditorDelegate)?](screcordingeditor/delegate.md)
### Instance Methods
- [func present(from: NSWindow, completionHandler: ((any Error)?) -> Void)](screcordingeditor/present(from:completionhandler:)-1nvxe.md)
- [func present(from: UIWindowScene, completionHandler: ((any Error)?) -> Void)](screcordingeditor/present(from:completionhandler:)-2atpt.md)
- [func present(from: UIWindowScene, mode: SCRecordingEditor.Mode, completionHandler: ((any Error)?) -> Void)](screcordingeditor/present(from:mode:completionhandler:).md)
### Enumerations
- [SCRecordingEditor.Mode](screcordingeditor/mode.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingeditor)*