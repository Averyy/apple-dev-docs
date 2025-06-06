# isDrawingFindIndicator

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view or one of its ancestors is being drawn for a find indicator.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isDrawingFindIndicator: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the view contents are being drawn so that they are easily readable against the find indicator background. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isdrawingfindindicator)*