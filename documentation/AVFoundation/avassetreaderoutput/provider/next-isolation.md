# next(isolation:)

**Framework**: AVFoundation  
**Kind**: method

Retruns the next piece of media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func next(isolation: isolated (any Actor)? = #isolation) async throws -> Payload?
```

#### Return Value

Returns the next piece of media data with the specified Payload type. If no more media data is available, this method returns nil.

#### Discussion

> **Note**: If the underlying reader encountered an error.

## Parameters

- `isolation`: The actor on which this async function should be isolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/next(isolation:))*