# NSTextStorage

**Framework**: AppKit  
**Kind**: class

The fundamental storage mechanism of TextKit that contains the text managed by the system.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class NSTextStorage
```

#### Overview

[`NSTextStorage`](nstextstorage.md) is a semi-concrete subclass of [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString) that adds behavior for managing a set of client [`NSLayoutManager`](nslayoutmanager.md) objects. A text storage object notifies its layout managers of changes to its characters or attributes, which lets the layout managers redisplay the text as needed.

You can access a text storage object from any thread of your app, but your app must guarantee access from only one thread at a time.

In macOS, this class also defines properties for getting and setting scriptable attributes of [`NSTextStorage`](nstextstorage.md) objects. Unless you’re dealing with scriptability, you shouldn’t access these properties directly. In particular, using the [`characters`](nstextstorage/characters.md), [`words`](nstextstorage/words.md), or [`paragraphs`](nstextstorage/paragraphs.md) properties is an inefficient way to manipulate the text storage, since accessing these properties involves the creation of many objects. Instead, use the text access methods defined by [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), [`NSMutableString`](https://developer.apple.com/documentation/Foundation/NSMutableString), and [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) to perform character-level manipulation.

##### Subclassing Notes

The [`NSTextStorage`](nstextstorage.md) class implements change management through the [`beginEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1411853-beginediting) and [`endEditing()`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1416707-endediting) methods, as well as verification of attributes, delegate handling, and layout management notification. The one aspect it doesn’t implement is managing the actual attributed string storage, which subclasses manage by overriding the two [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) primitives:

- [`string`](https://developer.apple.com/documentation/foundation/nsattributedstring/1412616-string)
- [`attributes(at:effectiveRange:)`](https://developer.apple.com/documentation/foundation/nsattributedstring/1415682-attributes)

Subclasses must also override two [`NSMutableAttributedString`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString) primitives:

- [`replaceCharacters(in:with:)`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1418451-replacecharacters)
- [`setAttributes(_:range:)`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1412179-setattributes)

These primitives should perform the change, then call [`edited(_:range:changeInLength:)`](nstextstorage/edited(_:range:changeinlength:).md) to let the parent class know there are changes.

## Topics

### Processing the editing actions
- [var delegate: (any NSTextStorageDelegate)?](nstextstorage/delegate.md)
  The delegate for the text storage object.
- [protocol NSTextStorageDelegate](nstextstoragedelegate.md)
  The optional methods that delegates of text storage objects implement to handle text-edit processing.
### Accessing the layout managers
- [var layoutManagers: [NSLayoutManager]](nstextstorage/layoutmanagers.md)
  The layout managers for the text storage object.
- [func addLayoutManager(NSLayoutManager)](nstextstorage/addlayoutmanager(_:).md)
  Adds a layout manager to the text storage object’s set of layout managers.
- [func removeLayoutManager(NSLayoutManager)](nstextstorage/removelayoutmanager(_:).md)
  Removes a layout manager from the text storage object’s set of layout managers.
### Managing edits
- [func edited(NSTextStorageEditActions, range: NSRange, changeInLength: Int)](nstextstorage/edited(_:range:changeinlength:).md)
  Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.
- [func processEditing()](nstextstorage/processediting.md)
  Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.
### Fixing the string attributes
- [func invalidateAttributes(in: NSRange)](nstextstorage/invalidateattributes(in:).md)
  Invalidates attributes in the specified range.
- [func ensureAttributesAreFixed(in: NSRange)](nstextstorage/ensureattributesarefixed(in:).md)
  Ensures that attribute fixing occurs in the specified range.
- [var fixesAttributesLazily: Bool](nstextstorage/fixesattributeslazily.md)
  A Boolean value that indicates whether the text storage object fixes attributes lazily.
### Determining the nature of changes
- [var editedMask: NSTextStorageEditActions](nstextstorage/editedmask.md)
  A mask that describes the kinds of edits pending for the text storage object.
- [var editedRange: NSRange](nstextstorage/editedrange.md)
  The range of text that contains changes.
- [var changeInLength: Int](nstextstorage/changeinlength.md)
  The difference between the current length of the edited range and its length before editing.
### Accessing scriptable properties
- [var attributeRuns: [NSTextStorage]](nstextstorage/attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var paragraphs: [NSTextStorage]](nstextstorage/paragraphs.md)
  The text storage contents as an array of paragraphs.
- [var words: [NSTextStorage]](nstextstorage/words.md)
  The text storage contents as an array of words.
- [var characters: [NSTextStorage]](nstextstorage/characters.md)
  The text storage contents as an array of characters.
- [var font: NSFont?](nstextstorage/font.md)
  The font for the text storage.
- [var foregroundColor: NSColor?](nstextstorage/foregroundcolor.md)
  The color for the text.
### Constants
- [struct NSTextStorageEditActions](nstextstorageeditactions.md)
  Constants that indicate the types of changes.
### Notifications
- [class let willProcessEditingNotification: NSNotification.Name](nstextstorage/willprocesseditingnotification.md)
  A notification that posts before a text storage begins processing edits.
- [class let didProcessEditingNotification: NSNotification.Name](nstextstorage/didprocesseditingnotification.md)
  A notification that posts after a text storage finishes processing edits.
### Accessing the storage controller
- [var textStorageObserver: (any NSTextStorageObserving)?](nstextstorage/textstorageobserver.md)
  The observer for the text storage object.
- [protocol NSTextStorageObserving](nstextstorageobserving.md)
  Optional methods that delegates implement to handle editing and transaction processing.

## Relationships

### Inherits From
- [NSMutableAttributedString](../Foundation/NSMutableAttributedString.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](nspasteboardreading.md)
- [NSPasteboardWriting](nspasteboardwriting.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSLayoutManager](nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.
- [class NSATSTypesetter](nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.
- [class NSTypesetter](nstypesetter.md)
  An abstract class that performs various type layout tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage)*