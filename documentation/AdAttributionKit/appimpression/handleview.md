# handleView()

**Framework**: AdAttributionKit  
**Kind**: method

Handles a view through ad impression.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst ?+

## Declaration

```swift
func handleView() async throws
```

## Mentions

- [Presenting ads in your app](presenting-ads-in-your-app.md)

#### Discussion

Call this method on the app impression to register a person’s viewing of the ad content.

## See Also

- [func beginView() async throws](appimpression/beginview.md)
  Begins recording a view-through impression when ad content corresponding to the impression becomes visible.
- [func endView() async throws](appimpression/endview.md)
  Ends the view-through impression when the ad content corresponding to the impression disappears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/handleview())*