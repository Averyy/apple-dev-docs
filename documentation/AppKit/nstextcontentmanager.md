# NSTextContentManager

**Framework**: AppKit  
**Kind**: class

An abstract class that defines the interface and a default implementation for managing the text document contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextContentManager
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

## Topics

### Creating a content manager
- [init()](nstextcontentmanager/init.md)
  Creates a new content manager.
- [init?(coder: NSCoder)](nstextcontentmanager/init(coder:).md)
  Creates a new content manager object from data in an unarchiver.
### Controlling backing store synchronization
- [var automaticallySynchronizesToBackingStore: Bool](nstextcontentmanager/automaticallysynchronizestobackingstore.md)
  Determines whether to automatically synchronize with the backing store when an editing transaction finishes.
### Performing transactions
- [var hasEditingTransaction: Bool](nstextcontentmanager/haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func performEditingTransaction(() -> Void)](nstextcontentmanager/performeditingtransaction(_:).md)
  Performs an editing transaction and invokes a block upon completion.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](nstextcontentmanager/recordeditaction(in:newtextrange:).md)
  Records information about an edit action to the transaction.
### Working with layout managers
- [var primaryTextLayoutManager: NSTextLayoutManager?](nstextcontentmanager/primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](nstextcontentmanager/textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/addtextlayoutmanager(_:).md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/removetextlayoutmanager(_:).md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](nstextcontentmanager/synchronizetextlayoutmanagers(_:).md)
  Synchronizes changes to all nonprimary text layout managers.
### Customizing and validating text elements
- [var delegate: (any NSTextContentManagerDelegate)?](nstextcontentmanager/delegate.md)
  The delegate for the content manager object.
- [protocol NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.
- [NSTextContentManager.EnumerationOptions](nstextcontentmanager/enumerationoptions.md)
  Values that control the order in which the framework enumerates text elements.
### Finding a specific text element
- [func textElements(for: NSTextRange) -> [NSTextElement]](nstextcontentmanager/textelements(for:).md)
  Returns an array of text elements that intersect with the range you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSTextContentStorage](nstextcontentstorage.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTextElementProvider](nstextelementprovider.md)

## See Also

- [class NSTextContentStorage](nstextcontentstorage.md)
  A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [class NSAttributedString](../Foundation/NSAttributedString.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](../Foundation/NSMutableAttributedString.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager)*