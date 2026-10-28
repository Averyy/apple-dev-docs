# editedRange

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The range of text that contains changes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var editedRange: NSRange { get }
```

```objc
@property (readonly) NSRange editedRange;
```

## Discussion

The specified range can reflect changes to characters or attributes. The text storage object’s delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

### Determining the nature of changes
- [var editedMask: NSTextStorageEditActions](./editedmask.md)
  A mask that describes the kinds of edits pending for the text storage object.
- [var changeInLength: Int](./changeinlength.md)
  The difference between the current length of the edited range and its length before editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/editedrange)*