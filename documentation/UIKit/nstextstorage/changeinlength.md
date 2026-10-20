# changeInLength

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The difference between the current length of the edited range and its length before editing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var changeInLength: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger changeInLength;
```

#### Discussion

This property reflects difference between the current length of the edited range and its length before editing began—that is, before the first call to the [`beginEditing()`](../../Foundation/nsmutableattributedstring/beginediting%28%29.md) method or a single call to the[`edited(_:range:changeInLength:)`](./edited%28_,range,changeinlength%29.md) method. This difference is accumulated with each call to the [`edited(_:range:changeInLength:)`](./edited%28_,range,changeinlength%29.md) method, until the changes are finally processed.

The text storage object’s delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

### Determining the nature of changes
- [var editedMask: NSTextStorage.EditActions](./editedmask.md)
  A mask that describes the kinds of edits pending for the text storage object.
- [var editedRange: NSRange](./editedrange.md)
  The range of text that contains changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/changeinlength)*