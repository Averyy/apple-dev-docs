# prominent

**Framework**: SwiftUI  
**Kind**: property

The prominent role.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var prominent: TabRole { get }
```

#### Discussion

A tab role that provides prominent visual treatment to one of the tabs in supported tab bars. Only one tab can receive the prominent treatment. When there are no tabs with an explicit `.prominent` role, then a `.search` role tab may receive the prominent visual treatment by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabrole/prominent)*