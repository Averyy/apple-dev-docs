# name

**Framework**: UIKit  
**Kind**: property

The name of the pasteboard.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var name: UIPasteboard.Name { get }
```

#### Discussion

Names of app pasteboard objects should be unique across installed apps. If the object is a system pasteboard, this property returns one of the constants described in [`Pasteboard Names`](pasteboard-names.md).

## See Also

- [init?(name: UIPasteboard.Name, create: Bool)](uipasteboard/init(name:create:).md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](uipasteboard/withuniquename.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
- [var changeCount: Int](uipasteboard/changecount.md)
  The number of times the pasteboard’s contents change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/name-swift.property)*