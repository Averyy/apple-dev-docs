# automatic

**Framework**: SwiftUI  
**Kind**: property

Determine the behavior automatically based on the surrounding context.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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