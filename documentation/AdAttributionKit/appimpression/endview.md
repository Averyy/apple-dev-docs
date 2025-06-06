# endView()

**Framework**: AdAttributionKit  
**Kind**: method

Ends the view-through impression when the ad content corresponding to the impression disappears.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
func endView() async throws
```

## Mentions

- [Presenting ads in your app](presenting-ads-in-your-app.md)

#### Discussion

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/appimpression/endview())*