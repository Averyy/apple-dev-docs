# cancelLoading()

**Framework**: AVFoundation  
**Kind**: method

Cancels all pending requests to asynchronously load property values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func cancelLoading()
```

#### Discussion

Calling this method cancels pending requests to load an asset’s property values. Call this method only when you’re done using an asset and you want to cancel any outstanding requests. Deallocating an asset implicitly calls this method if loading requests are still pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/cancelloading())*