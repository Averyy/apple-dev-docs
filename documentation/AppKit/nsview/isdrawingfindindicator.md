# isDrawingFindIndicator

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view or one of its ancestors is being drawn for a find indicator.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isDrawingFindIndicator: Bool { get }
```

```objc
@property (readonly, getter=isDrawingFindIndicator) BOOL drawingFindIndicator;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the view contents are being drawn so that they are easily readable against the find indicator background. The default value of this property is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isdrawingfindindicator)*