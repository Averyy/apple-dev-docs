# init(title:color:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
init(title: String, color: UIColor, handler: @escaping CPAlertActionHandler)
```

```objc
- (instancetype) initWithTitle:(NSString *) title color:(UIColor *) color handler:(CPAlertActionHandler) handler;
```

## See Also

### Creating an alert action
- [init(title: String, style: CPAlertAction.Style, handler: CPAlertActionHandler)](./init%28title,style,handler%29.md)
  Creates an alert action with a title, style, and action handler.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertaction/init(title:color:handler:))*