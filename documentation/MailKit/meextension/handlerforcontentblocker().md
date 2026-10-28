# handlerForContentBlocker()

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method

Returns an object that provides rules that the message viewer uses to block content.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func handlerForContentBlocker() -> any MEContentBlocker
```

```objc
- (id<MEContentBlocker>) handlerForContentBlocker;
```

## Return Value

An object that provides rules for blocking content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension/handlerforcontentblocker())*