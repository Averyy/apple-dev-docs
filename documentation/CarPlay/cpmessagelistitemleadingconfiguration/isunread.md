# isUnread

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the unread status of the conversation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isUnread: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isUnread) BOOL unread;
```

## Discussion

Specify this value at initialization time. When the value of this property is `true`, CarPlay displays an unread indicator in the row’s leading region. When the value is `false`, CarPlay doesn’t display this indicator.

## See Also

### Getting the configuration’s state
- [var leadingImage: UIImage?](./leadingimage.md)
  The custom image to display in the row’s leading region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemleadingconfiguration/isunread)*