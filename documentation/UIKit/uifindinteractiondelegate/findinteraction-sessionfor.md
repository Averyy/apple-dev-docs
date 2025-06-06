# findInteraction(_:sessionFor:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Provides the object for managing the state, presentation, and behavior of the search.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func findInteraction(_ interaction: UIFindInteraction, sessionFor view: UIView) -> UIFindSession?
```

#### Return Value

Returns an object the find interaction uses to manage the state, presentation, and behavior of the search. To prevent the find panel from appearing, return `nil`.

#### Discussion

Implement the [`UITextSearching`](uitextsearching-53wjq.md) protocol on the class that encapsulates the searchable content for your view to use an instance of [`UITextSearchingFindSession`](uitextsearchingfindsession.md) as the session object. Alternatively, you can subclass [`UIFindSession`](uifindsession.md) to manage the details of the session using a custom class.

## Parameters

- `interaction`: The interaction object triggering the find panel.
- `view`: The view you provide a find session object for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteractiondelegate/findinteraction(_:sessionfor:))*