# progress

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A value that indicates the progress of the export.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use `progressStates(updateInterval:)` instead.

## Declaration

```swift
var progress: Float { get }
```

```objc
@property (nonatomic, readonly) float progress;
```

#### Discussion

The value of this property ranges from `0.0` to `1.0.`


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/progress)*