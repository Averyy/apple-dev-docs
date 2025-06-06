# register(_:forItemIdentifier:)

**Framework**: AppKit  
**Kind**: method

Registers a nib file for the scrubber to use when it creates new items in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func register(_ nib: NSNib?, forItemIdentifier itemIdentifier: NSUserInterfaceItemIdentifier)
```

## Parameters

- `nib`: The nib object containing the item object. The nib file must contain exactly one top-level   object. You can use a custom subclass when configuring the object in the nib file. Specify   to unregister a previously registered file.
- `itemIdentifier`: The string that identifies the type of items. You use this string later when requesting new items. The string must be unique among the other registered item view classes of this scrubber. This parameter must not be an empty string or  .

## See Also

- [func register(AnyClass?, forItemIdentifier: NSUserInterfaceItemIdentifier)](nsscrubber/register(_:foritemidentifier:)-2rb69.md)
  Registers a class for the scrubber to use when it creates new items.
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSScrubberItemView?](nsscrubber/makeitem(withidentifier:owner:).md)
  Creates or returns a reusable item object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/register(_:foritemidentifier:)-6jye0)*