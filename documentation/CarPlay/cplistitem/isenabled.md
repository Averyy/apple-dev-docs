# isEnabled

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is enabled.

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

The default value of this property is `true`. Set the property to `false` to disable the item in your list interface. CarPlay doesn’t report interactions with disabled items and changes their appearance to reflect their disabled state.

## See Also

### Responding to interactions
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](./handler.md)
  The closure to run when someone interacts with any part of the list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/isenabled)*