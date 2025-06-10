# insertDebugSignpost(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Inserts a debug string into the frame data to aid debugging.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func insertDebugSignpost(_ string: String)
```

#### Discussion

Calling this method doesn’t change any behaviors, but can be useful for debugging purposes.

## Parameters

- `string`: The debug string to insert as a signpost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/insertdebugsignpost(_:))*