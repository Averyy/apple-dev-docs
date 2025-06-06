# cellState()

**Framework**: Quartz  
**Kind**: method

Returns the current cell state of the receiver.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func cellState() -> IKImageBrowserCellState
```

#### Return Value

The current state of the cell. See [`IKImageBrowserCellState`](ikimagebrowsercellstate.md) for possible values.

#### Discussion

The [`IKImageBrowserView`](ikimagebrowserview.md) creates thumbnails asynchronously. This method returns the current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell/cellstate())*