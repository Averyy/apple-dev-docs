# NSColorSampler

**Framework**: AppKit  
**Kind**: class

An object that displays the system’s color-sampling interface and returns the selected color to your app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSColorSampler
```

#### Overview

Create an [`NSColorSampler`](nscolorsampler.md) object when you want the user to select a color based on existing onscreen colors. When you call the [`show(selectionHandler:)`](nscolorsampler/show(selectionhandler:).md) method, AppKit shows the system’s color sampler interface and reports the selected color back to the provided block.

## Topics

### Capturing a Color Sample
- [func show(selectionHandler: (NSColor?) -> Void)](nscolorsampler/show(selectionhandler:).md)
  Displays the system color-sampling interface asynchronously and reports the selected color back to your app.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorsampler)*