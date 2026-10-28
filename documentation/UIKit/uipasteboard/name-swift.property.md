# name

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) UIPasteboardName name;
```

## Discussion

Names of app pasteboard objects should be unique across installed apps. If the object is a system pasteboard, this property returns one of the constants described in [Pasteboard Names](../pasteboard-names.md).

## See Also

### Related Documentation
- [init?(name: UIPasteboard.Name, create: Bool)](./init%28name,create%29.md)
  Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [class func withUniqueName() -> UIPasteboard](./withuniquename%28%29.md)
  Returns an app pasteboard that you identify by a unique system-generated name.
### Getting and setting pasteboard attributes
- [var changeCount: Int](./changecount.md)
  The number of times the pasteboard’s contents change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/name-swift.property)*