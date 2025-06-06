# candidateListTouchBarItem(_:changedCandidateListVisibility:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the visibility of the candidate list has changed.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func candidateListTouchBarItem(_ anItem: NSCandidateListTouchBarItem<AnyObject>, changedCandidateListVisibility isVisible: Bool)
```

## Parameters

- `anItem`: The candidate list item whose candidate list’s visibility has changed.
- `isVisible`: A Boolean value that specifies whether or not the candidate list is visible. If   then the candidate list is visible,   otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscandidatelisttouchbaritemdelegate/candidatelisttouchbaritem(_:changedcandidatelistvisibility:))*