# beginView()

**Framework**: AdAttributionKit  
**Kind**: method

Begins recording a view-through impression when ad content corresponding to the impression becomes visible.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
func beginView() async throws
```

#### Discussion

Begin the view impression process by calling [`beginView()`](appimpression/beginview().md), as  the following example shows:

```swift
   func handleAdAppeared(impression: AppImpression) async {
       do {
           try await impression.beginView()
       }
       catch {
           print("Failed to begin view-through impression: \(error).")
       }
   }
```

## See Also

- [func endView() async throws](appimpression/endview.md)
  Ends the view-through impression when the ad content corresponding to the impression disappears.
- [func handleView() async throws](appimpression/handleview.md)
  Handles a view through ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/beginview())*