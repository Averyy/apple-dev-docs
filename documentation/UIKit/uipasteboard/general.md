# general

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The systemwide general pasteboard, which you use for general copy-paste operations.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class var general: UIPasteboard { get }
```

```objc
@property (class, nonatomic, readonly) UIPasteboard * generalPasteboard;
```

## Return Value

A shared system pasteboard object with the name of [`general`](./name-swift.struct/general.md).

## Discussion

You may use the general pasteboard for copying and pasting text, images, URLs, colors, and other data within an app or between apps. The general pasteboard is persistent across device restarts and app uninstalls.

## See Also

### Getting and removing pasteboards
- [init?(name: UIPasteboard.Name, create: Bool)](./init%28name,create%29.md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](./withuniquename%28%29.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
- [class func remove(withName: UIPasteboard.Name)](./remove%28withname%29.md)
  Invalidates the designated app pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/general)*