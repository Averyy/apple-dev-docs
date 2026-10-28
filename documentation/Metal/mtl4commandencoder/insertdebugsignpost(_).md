# insertDebugSignpost(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Inserts a debug string into the frame data to aid debugging.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func insertDebugSignpost(_ string: String)
```

```objc
- (void) insertDebugSignpost:(NSString *) string;
```

## Discussion

Calling this method doesn’t change any behaviors, but can be useful for debugging purposes.

## Parameters

- `string`: The debug string to insert as a signpost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandencoder/insertdebugsignpost(_:))*