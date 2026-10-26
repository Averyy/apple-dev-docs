# init(image:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a message compose button that displays a custom image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(image: UIImage)
```

```objc
- (instancetype) initWithImage:(UIImage *) image;
```

#### Return Value

A message compose button with the custom image.

#### Discussion

> **Note**:  This button type does not use a handler. Instead, tapping this button activates Siri and initiates the compose message flow.

## Parameters

- `image`: The image to display on the button.

## See Also

### Creating a Message Compose Bar Button
- [init()](./init%28%29.md)
  Creates a message compose button with a system-provided image.
- [+ new](./new.md)
  Creates a message compose button with a system-provided image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton/init(image:))*