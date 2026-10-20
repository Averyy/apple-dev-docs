# windows

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The windows available for capture.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var windows: [SCWindow] { get }
```

```objc
@property (readonly) NSArray<SCWindow *> * windows;
```

## See Also

### Inspecting shareable content
- [var displays: [SCDisplay]](./displays.md)
  The displays available for capture.
- [var applications: [SCRunningApplication]](./applications.md)
  The apps available for capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/windows)*