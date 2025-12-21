# prepareContent()

**Framework**: AppKit  
**Kind**: method

Typically overridden by subclasses that require additional control over the creation of new objects.

**Availability**:
- macOS ?+

## Declaration

```swift
func prepareContent()
```

#### Discussion

Subclasses that implement this method are responsible for creating the new content object and setting it as the receiver’s content object. This method is only called if [`automaticallyPreparesContent`](nsobjectcontroller/automaticallypreparescontent.md) has been set to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var content: Any?](nsobjectcontroller/content.md)
  The receiver’s content object.
- [var automaticallyPreparesContent: Bool](nsobjectcontroller/automaticallypreparescontent.md)
  A Boolean that shows whether the receiver automatically creates and inserts new content objects automatically when loading from a nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/preparecontent())*