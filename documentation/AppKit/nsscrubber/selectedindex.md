# selectedIndex

**Framework**: AppKit  
**Kind**: property

The index of the selected item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var selectedIndex: Int { get set }
```

#### Discussion

If no item is selected, the value of this property is `-1`. If you set this property through the scrubber’s animator proxy, the selection change animates.

To use a scrubber’s animator proxy when changing the selected item, employ the [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md) protocol, using code like this: `scrubber.animator.selectedIndex = 123`

## See Also

- [var numberOfItems: Int](nsscrubber/numberofitems.md)
  The number of items represented by the scrubber.
- [var highlightedIndex: Int](nsscrubber/highlightedindex.md)
  The index of the highlighted item in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/selectedindex)*