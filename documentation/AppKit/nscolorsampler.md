# NSColorSampler

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that displays the system’s color-sampling interface and returns the selected color to your app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSColorSampler
```

```objc
@interface NSColorSampler : NSObject
```

## Overview

Create an [`NSColorSampler`](./nscolorsampler.md) object when you want the user to select a color based on existing onscreen colors. When you call the [`show(selectionHandler:)`](./nscolorsampler/show%28selectionhandler%29.md) method, AppKit shows the system’s color sampler interface and reports the selected color back to the provided block.

## Topics

### Capturing a Color Sample
- [func show(selectionHandler: (NSColor?) -> Void)](./nscolorsampler/show%28selectionhandler%29.md)
  Displays the system color-sampling interface asynchronously and reports the selected color back to your app.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorsampler)*