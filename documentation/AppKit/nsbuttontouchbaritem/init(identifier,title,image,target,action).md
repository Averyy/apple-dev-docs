# init(identifier:title:image:target:action:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

*Mac Catalyst*

```swift
convenience init(identifier: NSTouchBarItem.Identifier, title: String, image: UIImage, target: Any?, action: Selector?)
```

*macOS*

```swift
convenience init(identifier: NSTouchBarItem.Identifier, title: String, image: NSImage, target: Any?, action: Selector?)
```

*Mac Catalyst*

```objc
+ (instancetype) buttonTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier title:(NSString *) title image:(UIImage *) image target:(id) target action:(SEL) action;
```

*macOS*

```objc
+ (instancetype) buttonTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier title:(NSString *) title image:(NSImage *) image target:(id) target action:(SEL) action;
```

## See Also

### Creating a button item
- [convenience init(identifier: NSTouchBarItem.Identifier, image: UIImage, target: Any?, action: Selector?)](./init%28identifier,image,target,action%29.md)
- [convenience init(identifier: NSTouchBarItem.Identifier, title: String, target: Any?, action: Selector?)](./init%28identifier,title,target,action%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttontouchbaritem/init(identifier:title:image:target:action:))*