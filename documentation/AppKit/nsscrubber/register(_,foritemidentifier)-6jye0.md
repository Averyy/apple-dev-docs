# register(_:forItemIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers a nib file for the scrubber to use when it creates new items in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func register(_ nib: NSNib?, forItemIdentifier itemIdentifier: NSUserInterfaceItemIdentifier)
```

```objc
- (void) registerNib:(NSNib *) nib forItemIdentifier:(NSUserInterfaceItemIdentifier) itemIdentifier;
```

## Parameters

- `nib`: The nib object containing the item object. The nib file must contain exactly one top-level [`NSScrubberItemView`](../nsscrubberitemview.md) object. You can use a custom subclass when configuring the object in the nib file. Specify `nil` to unregister a previously registered file.
- `itemIdentifier`: The string that identifies the type of items. You use this string later when requesting new items. The string must be unique among the other registered item view classes of this scrubber. This parameter must not be an empty string or `nil`.

## See Also

### Creating scrubber items
- [func register(AnyClass?, forItemIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemidentifier%29-2rb69.md)
  Registers a class for the scrubber to use when it creates new items.
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSScrubberItemView?](./makeitem%28withidentifier,owner%29.md)
  Creates or returns a reusable item object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/register(_:foritemidentifier:)-6jye0)*