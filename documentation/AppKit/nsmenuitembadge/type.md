# type

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of items the badge displays.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var type: NSMenuItemBadge.BadgeType { get }
```

```objc
@property (readonly) NSMenuItemBadgeType type;
```

#### Discussion

If you create a badge with a custom string, this value is [`NSMenuItemBadge.BadgeType.none`](./badgetype/none.md).

## See Also

### Accessing menu item badge attributes
- [var itemCount: Int](./itemcount.md)
  The number of items the badge displays.
- [var stringValue: String?](./stringvalue-fc9f.md)
  The string representation of the badge when it displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/type)*