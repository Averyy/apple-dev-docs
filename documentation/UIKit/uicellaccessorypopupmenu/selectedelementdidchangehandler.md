# selectedElementDidChangeHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An optional closure that the system calls when a user selects an element in the menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^selectedElementDidChangeHandler)(UIMenu *menu);
```

## See Also

### Accessing configuration options
- [menu](./menu.md)
  The menu to display when a user taps the popup menu accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessorypopupmenu/selectedelementdidchangehandler)*