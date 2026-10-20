# wantsDefaultContentAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Determines whether the default content appearance should be used for the popover.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: The system no longer supports this feature.

## Declaration

```swift
class var wantsDefaultContentAppearance: Bool { get }
```

```objc
@property (class, nonatomic, readonly) BOOL wantsDefaultContentAppearance;
```

#### Discussion

This method may be overridden to prevent the drawing of the content inset and drop shadow inside the popover. The default implementation of this method returns [`true`](../../Swift/true.md), which means that the content inset and drop shadow will be drawn. Overriding this method simply means implementing it to return [`false`](../../Swift/false.md), which would mean that the content inset and drop shadow will not be drawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/wantsdefaultcontentappearance)*