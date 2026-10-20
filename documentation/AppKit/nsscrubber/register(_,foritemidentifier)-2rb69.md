# register(_:forItemIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers a class for the scrubber to use when it creates new items.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func register(_ itemViewClass: AnyClass?, forItemIdentifier itemIdentifier: NSUserInterfaceItemIdentifier)
```

```objc
- (void) registerClass:(Class) itemViewClass forItemIdentifier:(NSUserInterfaceItemIdentifier) itemIdentifier;
```

## Parameters

- `itemViewClass`: A class to use for creating items. The class must be descended from [`NSScrubberItemView`](../nsscrubberitemview.md). Specify `nil` to unregister a previously registered class.
- `itemIdentifier`: The string that identifies the type of item. You use this string later when requesting new item views. The string must be unique among the other registered item view classes of this scrubber. This parameter must not be an empty string or `nil`.

## See Also

### Creating scrubber items
- [func register(NSNib?, forItemIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemidentifier%29-6jye0.md)
  Registers a nib file for the scrubber to use when it creates new items in the scrubber.
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSScrubberItemView?](./makeitem%28withidentifier,owner%29.md)
  Creates or returns a reusable item object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/register(_:foritemidentifier:)-2rb69)*