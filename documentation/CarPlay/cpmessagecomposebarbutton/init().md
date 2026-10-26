# init()

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a message compose button with a system-provided image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

A message compose button with a system-provided image.

#### Discussion

> **Note**:  This button type does not use a handler. Instead, tapping this button activates Siri and initiates the compose message flow.

## See Also

### Creating a Message Compose Bar Button
- [init(image: UIImage)](./init%28image%29.md)
  Creates a message compose button that displays a custom image.
- [+ new](./new.md)
  Creates a message compose button with a system-provided image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagecomposebarbutton/init())*