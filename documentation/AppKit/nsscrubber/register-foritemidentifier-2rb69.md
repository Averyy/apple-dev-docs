# register(_:forItemIdentifier:)

**Framework**: AppKit  
**Kind**: method

Registers a class for the scrubber to use when it creates new items.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func register(_ itemViewClass: AnyClass?, forItemIdentifier itemIdentifier: NSUserInterfaceItemIdentifier)
```

## Parameters

- `itemViewClass`: A class to use for creating items. The class must be descended from  . Specify   to unregister a previously registered class.
- `itemIdentifier`: The string that identifies the type of item. You use this string later when requesting new item views. The string must be unique among the other registered item view classes of this scrubber. This parameter must not be an empty string or  .

## See Also

- [func register(NSNib?, forItemIdentifier: NSUserInterfaceItemIdentifier)](nsscrubber/register(_:foritemidentifier:)-6jye0.md)
  Registers a nib file for the scrubber to use when it creates new items in the scrubber.
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSScrubberItemView?](nsscrubber/makeitem(withidentifier:owner:).md)
  Creates or returns a reusable item object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/register(_:foritemidentifier:)-2rb69)*