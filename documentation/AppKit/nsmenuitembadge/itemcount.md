# itemCount

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of items the badge displays.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var itemCount: Int { get }
```

```objc
@property (readonly) NSInteger itemCount;
```

## Discussion

If you create a badge with a custom string, this value is `0`.

## See Also

### Accessing menu item badge attributes
- [var stringValue: String?](./stringvalue-fc9f.md)
  The string representation of the badge when it displays.
- [var type: NSMenuItemBadge.BadgeType](./type.md)
  The type of items the badge displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitembadge/itemcount)*