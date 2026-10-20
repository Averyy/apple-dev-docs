# orderedDocuments

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of document objects arranged according to the front-to-back ordering of their associated windows.

**Availability**:
- macOS

## Declaration

```swift
var orderedDocuments: [NSDocument] { get }
```

```objc
@property (copy, readonly) NSArray<NSDocument *> * orderedDocuments;
```

## See Also

### Scripting your app
- [var orderedWindows: [NSWindow]](./orderedwindows.md)
  An array of window objects arranged according to their front-to-back ordering on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/ordereddocuments)*