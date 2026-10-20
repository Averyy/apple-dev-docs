# automaticallyPreparesContent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that shows whether the receiver automatically creates and inserts new content objects automatically when loading from a nib file.

**Availability**:
- macOS

## Declaration

```swift
var automaticallyPreparesContent: Bool { get set }
```

```objc
@property BOOL automaticallyPreparesContent;
```

#### Discussion

If `flag` is [`true`](../../Swift/true.md) and the receiver is not using a managed object context, [`prepareContent()`](./preparecontent%28%29.md) is used to create the content object. If `flag` is [`true`](../../Swift/true.md) and a managed object context is set, the initial content is fetched from the managed object context using the current fetch predicate. The default is [`false`](../../Swift/false.md).

## See Also

### Managing content
- [var content: Any?](./content.md)
  The receiver’s content object.
- [func prepareContent()](./preparecontent%28%29.md)
  Typically overridden by subclasses that require additional control over the creation of new objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/automaticallypreparescontent)*