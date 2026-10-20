# handleView()

**Framework**: AdAttributionKit  
**Kind**: method  
**Role**: Instance Method

Handles a view through ad impression.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
func handleView() async throws
```

## Mentions

- [Presenting ads in your app](../presenting-ads-in-your-app.md)

#### Discussion

Call this method on the app impression to register a person’s viewing of the ad content.

## See Also

### Displaying view-through ads
- [func beginView() async throws](./beginview%28%29.md)
  Begins recording a view-through impression when ad content corresponding to the impression becomes visible.
- [func endView() async throws](./endview%28%29.md)
  Ends the view-through impression when the ad content corresponding to the impression disappears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/handleview())*