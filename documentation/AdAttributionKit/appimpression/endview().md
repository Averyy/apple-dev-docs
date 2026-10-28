# endView()

**Framework**: AdAttributionKit  
**Kind**: method  
**Role**: Instance Method

Ends the view-through impression when the ad content corresponding to the impression disappears.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
func endView() async throws
```

## Discussion

End the view-through impression, as the following example shows:

```swift
   func handleAdDisappeared(impression: AppImpression) async {
       do {
           try await impression.endView()
       }
       catch {
           print("Failed to end view-through impression: \(error).")
       }
   }    
```

## See Also

### Displaying view-through ads
- [func beginView() async throws](./beginview%28%29.md)
  Begins recording a view-through impression when ad content corresponding to the impression becomes visible.
- [func handleView() async throws](./handleview%28%29.md)
  Handles a view through ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/endview())*