# scrollItem(at:to:)

**Framework**: AppKit  
**Kind**: method

Scrolls an item to a specified alignment within the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func scrollItem(at index: Int, to alignment: NSScrubber.Alignment)
```

#### Discussion

To animate the scroll, call this method on the animator proxy. See [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md) for details.

## Parameters

- `index`: The index of the item to be scrolled. Indexes range between   and  , where   is the number of items displayed in the scrubber.
- `alignment`: The position the item should be scrolled to. For possible values, see  . If  , the scrubber scrolls the minimum distance required to make the item visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/scrollitem(at:to:))*