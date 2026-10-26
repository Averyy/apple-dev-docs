# NSTextContentManager

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract class that defines the interface and a default implementation for managing the text document contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextContentManager
```

```objc
@interface NSTextContentManager : NSObject
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](./adding-writing-tools-support-to-a-custom-nsview.md)

## Topics

### Creating a content manager
- [init()](./nstextcontentmanager/init%28%29.md)
  Creates a new content manager.
- [init?(coder: NSCoder)](./nstextcontentmanager/init%28coder%29.md)
  Creates a new content manager object from data in an unarchiver.
### Controlling backing store synchronization
- [var automaticallySynchronizesToBackingStore: Bool](./nstextcontentmanager/automaticallysynchronizestobackingstore.md)
  Determines whether to automatically synchronize with the backing store when an editing transaction finishes.
### Performing transactions
- [var hasEditingTransaction: Bool](./nstextcontentmanager/haseditingtransaction.md)
  Indicates there’s an active editing transaction from the primary text layout manager.
- [func performEditingTransaction(() -> Void)](./nstextcontentmanager/performeditingtransaction%28_%29.md)
  Performs an editing transaction and invokes a block upon completion.
- [func recordEditAction(in: NSTextRange, newTextRange: NSTextRange)](./nstextcontentmanager/recordeditaction%28in,newtextrange%29.md)
  Records information about an edit action to the transaction.
### Working with layout managers
- [var primaryTextLayoutManager: NSTextLayoutManager?](./nstextcontentmanager/primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](./nstextcontentmanager/textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](./nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](./nstextcontentmanager/addtextlayoutmanager%28_%29.md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](./nstextcontentmanager/removetextlayoutmanager%28_%29.md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](./nstextcontentmanager/synchronizetextlayoutmanagers%28_%29.md)
  Synchronizes changes to all nonprimary text layout managers.
### Customizing and validating text elements
- [var delegate: (any NSTextContentManagerDelegate)?](./nstextcontentmanager/delegate.md)
  The delegate for the content manager object.
- [protocol NSTextContentManagerDelegate](./nstextcontentmanagerdelegate.md)
  The optional methods that delegates of content manager objects implement for customizing or validating text elements.
- [NSTextContentManager.EnumerationOptions](./nstextcontentmanager/enumerationoptions.md)
  Values that control the order in which the framework enumerates text elements.
### Finding a specific text element
- [func textElements(for: NSTextRange) -> [NSTextElement]](./nstextcontentmanager/textelements%28for%29.md)
  Returns an array of text elements that intersect with the range you specify.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSTextContentStorage](./nstextcontentstorage.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NSTextElementProvider](./nstextelementprovider.md)

## See Also

### Text management
- [class NSTextContentStorage](./nstextcontentstorage.md)
  A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [class NSAttributedString](../Foundation/nsattributedstring.md)
  A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [class NSMutableAttributedString](../Foundation/nsmutableattributedstring.md)
  A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.
- [TextKit string attributes](./textkit-string-attributes.md)
  AppKit-specific keys and values for displaying text and managing documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager)*