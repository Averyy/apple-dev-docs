# automaticallyPreparesContent

**Framework**: AppKit  
**Kind**: property

A Boolean that shows whether the receiver automatically creates and inserts new content objects automatically when loading from a nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
var automaticallyPreparesContent: Bool { get set }
```

#### Discussion

If `flag` is [`true`](https://developer.apple.com/documentation/swift/true) and the receiver is not using a managed object context, [`prepareContent()`](nsobjectcontroller/preparecontent().md) is used to create the content object. If `flag` is [`true`](https://developer.apple.com/documentation/swift/true) and a managed object context is set, the initial content is fetched from the managed object context using the current fetch predicate. The default is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var content: Any?](nsobjectcontroller/content.md)
  The receiver’s content object.
- [func prepareContent()](nsobjectcontroller/preparecontent.md)
  Typically overridden by subclasses that require additional control over the creation of new objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/automaticallypreparescontent)*