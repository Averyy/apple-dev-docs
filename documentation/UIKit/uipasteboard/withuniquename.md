# withUniqueName()

**Framework**: UIKit  
**Kind**: method

Returns an app pasteboard that you identify by a unique system-generated name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func withUniqueName() -> UIPasteboard
```

#### Return Value

An app pasteboard object with a unique name.

#### Discussion

Obtain the value of the [`name`](uipasteboard/name-swift.property.md) property to discover the name of the returned pasteboard. App pasteboards returned by this method are not persistent, existing only until the app quits. Starting in iOS 10, persistent named pasteboards are deprecated. Instead use a shared container, as described in the overview for the [`UIPasteboard`](uipasteboard.md) class.

## See Also

- [class var general: UIPasteboard](uipasteboard/general.md)
  The systemwide general pasteboard, which you use for general copy-paste operations.
- [init?(name: UIPasteboard.Name, create: Bool)](uipasteboard/init(name:create:).md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func remove(withName: UIPasteboard.Name)](uipasteboard/remove(withname:).md)
  Invalidates the designated app pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/withuniquename())*