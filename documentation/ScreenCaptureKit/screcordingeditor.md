# SCRecordingEditor

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class SCRecordingEditor
```

```objc
@interface SCRecordingEditor : NSObject
```

#### Overview

Presents a system-owned preview UI for a completed recording via SCStream.

SCRecordingEditor owns the full presentation lifecycle of the preview UI. Callers provide an optional anchor window (macOS) or scene; if none is provided, the foreground window/scene is discovered automatically.

## Topics

### Initializers
- [init(URL: URL)](./screcordingeditor/init%28url%29-1k2cv.md)
- [init(url: URL)](./screcordingeditor/init%28url%29-ead5.md)
### Instance Properties
- [var delegate: (any SCRecordingEditorDelegate)?](./screcordingeditor/delegate.md)
### Instance Methods
- [func present(from: NSWindow, completionHandler: ((any Error)?) -> Void)](./screcordingeditor/present%28from,completionhandler%29-1nvxe.md)
- [func present(from: UIWindowScene, completionHandler: ((any Error)?) -> Void)](./screcordingeditor/present%28from,completionhandler%29-2atpt.md)
- [func present(from: UIWindowScene, mode: SCRecordingEditor.Mode, completionHandler: ((any Error)?) -> Void)](./screcordingeditor/present%28from,mode,completionhandler%29.md)
### Enumerations
- [SCRecordingEditor.Mode](./screcordingeditor/mode.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/screcordingeditor)*