# init(title:textStyle:handler:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a button that displays a title in a specific style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(title: String, textStyle: CPTextButtonStyle, handler: ((CPTextButton) -> Void)? = nil)
```

```objc
- (instancetype) initWithTitle:(NSString *) title textStyle:(CPTextButtonStyle) textStyle handler:(void (^)(CPTextButton *contactButton)) handler;
```

## Parameters

- `title`: The text that the button displays.
- `textStyle`: The style that the button applies to its title.
- `handler`: A closure that CarPlay invokes when the user taps the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptextbutton/init(title:textstyle:handler:))*