# content

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s content object.

**Availability**:
- macOS

## Declaration

```swift
var content: Any? { get set }
```

```objc
@property (strong, nullable) id content;
```

## See Also

### Managing content
- [var automaticallyPreparesContent: Bool](./automaticallypreparescontent.md)
  A Boolean that shows whether the receiver automatically creates and inserts new content objects automatically when loading from a nib file.
- [func prepareContent()](./preparecontent%28%29.md)
  Typically overridden by subclasses that require additional control over the creation of new objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/content)*