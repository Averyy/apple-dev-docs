# capturesMouseClicks

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether mouse clicks appear highlighted in the captured output.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var capturesMouseClicks: Bool { get set }
```

#### Discussion

By default, `AVCaptureScreenInput` does not highlight mouse clicks in its captured output.

If you set this property is set to [`true`](https://developer.apple.com/documentation/swift/true), mouse clicks are highlighted (a circle is drawn around the mouse for the duration of the click) in the captured output.

## See Also

- [var capturesCursor: Bool](avcapturescreeninput/capturescursor.md)
  A Boolean value that specifies whether the mouse cursor appears in the captured output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/capturesmouseclicks)*