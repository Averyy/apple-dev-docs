# init(title:style:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates an alert action with a title, style, and action handler.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(title: String, style: CPAlertAction.Style, handler: @escaping CPAlertActionHandler)
```

```objc
- (instancetype) initWithTitle:(NSString *) title style:(CPAlertActionStyle) style handler:(CPAlertActionHandler) handler;
```

## Return Value

A newly initialized alert action.

## Parameters

- `title`: The title displayed on the action button.
- `style`: The display style for the action button.
- `handler`: The block invoked after the user taps the action button.

## See Also

### Creating an alert action
- [init(title: String, color: UIColor, handler: CPAlertActionHandler)](./init%28title,color,handler%29.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalertaction/init(title:style:handler:))*