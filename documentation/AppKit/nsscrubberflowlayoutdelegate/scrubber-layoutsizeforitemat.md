# scrubber(_:layout:sizeForItemAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate for the size of each item in a scrubber whose items are arranged in a flow layout.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
optional func scrubber(_ scrubber: NSScrubber, layout: NSScrubberFlowLayout, sizeForItemAt itemIndex: Int) -> NSSize
```

#### Return Value

The width and height of the item at the specified index in the scrubber.

## Parameters

- `scrubber`: The scrubber object displaying the items arranged in a flow layout.
- `layout`: The layout object requesting the information.
- `itemIndex`: The index of the item in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberflowlayoutdelegate/scrubber(_:layout:sizeforitemat:))*