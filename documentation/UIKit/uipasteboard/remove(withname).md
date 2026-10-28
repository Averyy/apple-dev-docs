# remove(withName:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Invalidates the designated app pasteboard.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func remove(withName pasteboardName: UIPasteboard.Name)
```

```objc
+ (void) removePasteboardWithName:(UIPasteboardName) pasteboardName;
```

## Discussion

Invalidation of an app pasteboard frees up all resources used by it. Once a pasteboard is invalidated, you cannot use the it; `UIPasteboard` ignores any calls to it. The method has no effect if called with the name of a system pasteboard.

## Parameters

- `pasteboardName`: The name of the pasteboard to be invalidated.

## See Also

### Getting and removing pasteboards
- [class var general: UIPasteboard](./general.md)
  The systemwide general pasteboard, which you use for general copy-paste operations.
- [init?(name: UIPasteboard.Name, create: Bool)](./init%28name,create%29.md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](./withuniquename%28%29.md)
  Returns an app pasteboard that you identify by a unique system-generated name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/remove(withname:))*