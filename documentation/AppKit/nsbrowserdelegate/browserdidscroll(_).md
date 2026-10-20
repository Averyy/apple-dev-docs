# browserDidScroll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the browser has scrolled.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browserDidScroll(_ sender: NSBrowser)
```

```objc
- (void) browserDidScroll:(NSBrowser *) sender;
```

## Parameters

- `sender`: The browser sending the message.

## See Also

### Scrolling
- [func browserWillScroll(NSBrowser)](./browserwillscroll%28_%29.md)
  Notifies the delegate when the browser will scroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browserdidscroll(_:))*