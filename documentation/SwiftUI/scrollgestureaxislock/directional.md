# directional

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Scroll gestures are locked to their predominant axis.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static var directional: ScrollGestureAxisLock { get }
```

## Discussion

On watchOS, this affects only touch panning, as Digital Crown scrolling already moves along only one axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollgestureaxislock/directional)*