# wantsDefaultContentAppearance

**Framework**: UIKit  
**Kind**: property

Determines whether the default content appearance should be used for the popover.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
class var wantsDefaultContentAppearance: Bool { get }
```

#### Discussion

This method may be overridden to prevent the drawing of the content inset and drop shadow inside the popover. The default implementation of this method returns [`true`](https://developer.apple.com/documentation/Swift/true), which means that the content inset and drop shadow will be drawn. Overriding this method simply means implementing it to return [`false`](https://developer.apple.com/documentation/Swift/false), which would mean that the content inset and drop shadow will not be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/wantsdefaultcontentappearance)*