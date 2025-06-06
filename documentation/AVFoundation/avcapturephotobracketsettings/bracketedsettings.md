# bracketedSettings

**Framework**: AVFoundation  
**Kind**: property

An array describing the number of and settings for images to produce in a bracketed capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var bracketedSettings: [AVCaptureBracketedStillImageSettings] { get }
```

#### Discussion

This array is read-only. You provide this array of bracket settings when creating a settings object with the `init(format:rawPixelFormatType:bracketedSettings:)` initializer.

## See Also

- [var isLensStabilizationEnabled: Bool](avcapturephotobracketsettings/islensstabilizationenabled.md)
  A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/bracketedsettings)*