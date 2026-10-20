# init(identifier:title:target:action:)

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
convenience init(identifier: NSTouchBarItem.Identifier, title: String, target: Any?, action: Selector?)
```

```objc
+ (instancetype) buttonTouchBarItemWithIdentifier:(NSTouchBarItemIdentifier) identifier title:(NSString *) title target:(id) target action:(SEL) action;
```

## See Also

### Creating a button item
- [convenience init(identifier: NSTouchBarItem.Identifier, image: UIImage, target: Any?, action: Selector?)](./init%28identifier,image,target,action%29.md)
- [convenience init(identifier: NSTouchBarItem.Identifier, title: String, image: UIImage, target: Any?, action: Selector?)](./init%28identifier,title,image,target,action%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttontouchbaritem/init(identifier:title:target:action:))*