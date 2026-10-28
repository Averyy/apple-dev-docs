# isSpringLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether spring loading is enabled for the control.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var isSpringLoaded: Bool { get set }
```

```objc
@property (getter=isSpringLoaded) BOOL springLoaded;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if spring loading is enabled for the control, and [`false`](../../Swift/false.md) if it is not. The default is [`false`](../../Swift/false.md).

On pressure-sensitive systems, such as systems with the Force Touch trackpad, spring loading is a feature that allows a user to activate a segment in a segmented control by dragging selected items over it and force clicking—pressing harder—without dropping the selected items. The user can then continue dragging the items, possibly to perform additional actions.

A practical example of this feature can be found in the Calendar app. A selected calendar event can be dragged over the day, week, month, or year segments in the toolbar. Force clicking on a segment switches the calendar view without releasing the selected calendar event. The calendar event can then be dropped at the desired location in the new calendar view.

When spring loading is enabled on a segmented control and a user drags something over a segment, the segment highlights to indicate that it responds to force clicking. In this situation, if the user presses harder, additional highlighting occurs to indicate that the segment was activated.

On systems that don’t support pressure sensitivity, simply hovering over the segment for a short period of time is sufficient to activate the segment.

## See Also

### Configuring a segment menu
- [func setMenu(NSMenu?, forSegment: Int)](./setmenu%28_,forsegment%29.md)
  Sets the menu for the specified segment.
- [func menu(forSegment: Int) -> NSMenu?](./menu%28forsegment%29.md)
  Returns the menu for the specified segment.
- [func setShowsMenuIndicator(Bool, forSegment: Int)](./setshowsmenuindicator%28_,forsegment%29.md)
- [func showsMenuIndicator(forSegment: Int) -> Bool](./showsmenuindicator%28forsegment%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/isspringloaded)*