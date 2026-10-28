# makeItem(withIdentifier:owner:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates or returns a reusable item object with the specified identifier.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func makeItem(withIdentifier itemIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSScrubberItemView?
```

```objc
- (NSScrubberItemView *) makeItemWithIdentifier:(NSUserInterfaceItemIdentifier) itemIdentifier owner:(id) owner;
```

## Return Value

A valid [`NSScrubberItemView`](../nsscrubberitemview.md) object.

## Parameters

- `itemIdentifier`: The string that identifies the type of item you want. This is the identifier you specified when registering the item view. The parameter must not be `nil`.
- `owner`: The owner of this item. If the scrubber item is loaded from a nib then this object is set as the nib’s File’s Owner object. Set this parameter to `nil` for scrubber items loaded from classes.

## See Also

### Creating scrubber items
- [func register(AnyClass?, forItemIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemidentifier%29-2rb69.md)
  Registers a class for the scrubber to use when it creates new items.
- [func register(NSNib?, forItemIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemidentifier%29-6jye0.md)
  Registers a nib file for the scrubber to use when it creates new items in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/makeitem(withidentifier:owner:))*