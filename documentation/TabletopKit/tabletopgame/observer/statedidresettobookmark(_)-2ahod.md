# stateDidResetToBookmark(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Called whenever a `jumpToBookmark` is applied to the shared network table state. `stateDidResetToBookmark` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks, and are also network delayed behind any changes to the speculative visible table state.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func stateDidResetToBookmark(_ bookmarkID: StateBookmarkIdentifier)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/statedidresettobookmark(_:)-2ahod)*