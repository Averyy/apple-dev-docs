# activeFindSession

**Framework**: UIKit  
**Kind**: property

The object that manages the state, presentation, and behavior of an active search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var activeFindSession: UIFindSession? { get }
```

#### Discussion

This property returns the session object managing the details of the search. When no seach is active, [`isFindNavigatorVisible`](uifindinteraction/isfindnavigatorvisible.md) is `false`, this returns `nil`.

## See Also

- [func updateResultCount()](uifindinteraction/updateresultcount.md)
  Updates the results the interface displays for the active search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/activefindsession)*