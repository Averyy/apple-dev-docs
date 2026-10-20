# browserWillScroll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the browser will scroll.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browserWillScroll(_ sender: NSBrowser)
```

```objc
- (void) browserWillScroll:(NSBrowser *) sender;
```

## Parameters

- `sender`: The browser sending the message.

## See Also

### Scrolling
- [func browserDidScroll(NSBrowser)](./browserdidscroll%28_%29.md)
  Notifies the delegate when the browser has scrolled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browserwillscroll(_:))*