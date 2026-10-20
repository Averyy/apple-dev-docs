# highlightedIndex

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the highlighted item in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var highlightedIndex: Int { get }
```

```objc
@property (readonly) NSInteger highlightedIndex;
```

#### Discussion

If no item is highlighted, the value of this property is `-1`.

## See Also

### Getting the state of the scrubber
- [var numberOfItems: Int](./numberofitems.md)
  The number of items represented by the scrubber.
- [var selectedIndex: Int](./selectedindex.md)
  The index of the selected item in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/highlightedindex)*