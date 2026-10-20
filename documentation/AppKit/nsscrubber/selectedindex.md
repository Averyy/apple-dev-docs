# selectedIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the selected item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var selectedIndex: Int { get set }
```

```objc
@property NSInteger selectedIndex;
```

#### Discussion

If no item is selected, the value of this property is `-1`. If you set this property through the scrubber’s animator proxy, the selection change animates.

To use a scrubber’s animator proxy when changing the selected item, employ the [`NSAnimatablePropertyContainer`](../nsanimatablepropertycontainer.md) protocol, using code like this: `scrubber.animator.selectedIndex = 123`

## See Also

### Getting the state of the scrubber
- [var numberOfItems: Int](./numberofitems.md)
  The number of items represented by the scrubber.
- [var highlightedIndex: Int](./highlightedindex.md)
  The index of the highlighted item in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/selectedindex)*