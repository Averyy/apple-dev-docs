# remove(withName:)

**Framework**: UIKit  
**Kind**: method

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

#### Discussion

Invalidation of an app pasteboard frees up all resources used by it. Once a pasteboard is invalidated, you cannot use the it; `UIPasteboard` ignores any calls to it. The method has no effect if called with the name of a system pasteboard.

## Parameters

- `pasteboardName`: The name of the pasteboard to be invalidated.

## See Also

- [class var general: UIPasteboard](uipasteboard/general.md)
  The systemwide general pasteboard, which you use for general copy-paste operations.
- [init?(name: UIPasteboard.Name, create: Bool)](uipasteboard/init(name:create:).md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](uipasteboard/withuniquename.md)
  Returns an app pasteboard that you identify by a unique system-generated name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/remove(withname:))*