# automatic

**Framework**: SwiftUI  
**Kind**: property

Determine the behavior automatically based on the surrounding context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static let automatic: TabBarMinimizeBehavior
```

#### Discussion

The depends on the platform:

- On iOS, iPadOS, tvOS, and watchOS, the tab bar does not minimize.
- On visionOS, the tab bar minimizes when people look away from it.
- On macOS, the tab bar minimizes when the window has reduced space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior/automatic)*