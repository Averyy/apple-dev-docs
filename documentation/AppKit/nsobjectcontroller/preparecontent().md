# prepareContent()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Typically overridden by subclasses that require additional control over the creation of new objects.

**Availability**:
- macOS

## Declaration

```swift
func prepareContent()
```

```objc
- (void) prepareContent;
```

#### Discussion

Subclasses that implement this method are responsible for creating the new content object and setting it as the receiver’s content object. This method is only called if [`automaticallyPreparesContent`](./automaticallypreparescontent.md) has been set to [`true`](../../Swift/true.md).

## See Also

### Managing content
- [var content: Any?](./content.md)
  The receiver’s content object.
- [var automaticallyPreparesContent: Bool](./automaticallypreparescontent.md)
  A Boolean that shows whether the receiver automatically creates and inserts new content objects automatically when loading from a nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/preparecontent())*