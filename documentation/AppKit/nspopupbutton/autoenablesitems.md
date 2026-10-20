# autoenablesItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the button enables and disables its items every time a user event occurs.

**Availability**:
- macOS

## Declaration

```swift
var autoenablesItems: Bool { get set }
```

```objc
@property BOOL autoenablesItems;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), user events cause the button to enable and disable its items automatically according to the NSMenuValidation protocol specification.

## See Also

### Setting the type of menu
- [var pullsDown: Bool](./pullsdown.md)
  A Boolean value indicating whether the button displays a pull-down or pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/autoenablesitems)*