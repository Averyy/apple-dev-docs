# init(image:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a button for composing messages that uses a custom image you provide.

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

## Return Value

An initialized bar button for composing messages

## Parameters

- `image`: The image to display in the button. Provide an image that scales to different sizes. For best results, initialize your image object with an SF Symbol.

## See Also

### Creating a message compose bar button
- [init()](./init%28%29.md)
  Creates a button for composing messages that uses the system-provided image.
- [+ new](./new.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton/init(image:))*