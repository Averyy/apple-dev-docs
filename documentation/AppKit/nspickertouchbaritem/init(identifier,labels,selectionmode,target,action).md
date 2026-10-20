# init(identifier:labels:selectionMode:target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
convenience init(identifier: NSTouchBarItem.Identifier, labels: [String], selectionMode: NSPickerTouchBarItem.SelectionMode, target: Any?, action: Selector?)
```

```objc
+ (instancetype) pickerTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier labels:(NSArray<NSString *> *) labels selectionMode:(NSPickerTouchBarItemSelectionMode) selectionMode target:(id) target action:(SEL) action;
```

## See Also

### Creating a picker item
- [convenience init(identifier: NSTouchBarItem.Identifier, images: [UIImage], selectionMode: NSPickerTouchBarItem.SelectionMode, target: Any?, action: Selector?)](./init%28identifier,images,selectionmode,target,action%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspickertouchbaritem/init(identifier:labels:selectionmode:target:action:))*