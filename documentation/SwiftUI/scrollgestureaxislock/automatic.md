# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Uses the platform’s default behavior for locking scroll gestures.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static var automatic: ScrollGestureAxisLock { get }
```

## Discussion

On macOS, scroll gestures lock to their predominant axis by default. On iOS, iPadOS, Mac Catalyst, visionOS, and watchOS, scroll gestures move along both axes at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollgestureaxislock/automatic)*