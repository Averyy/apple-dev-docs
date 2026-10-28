# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the item is enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Managing Configuration
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.
- [var userInfo: Any?](./userinfo.md)
  An opaque value for the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/isenabled)*