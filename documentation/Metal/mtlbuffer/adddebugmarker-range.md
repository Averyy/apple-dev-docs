# addDebugMarker(_:range:)

**Framework**: Metal  
**Kind**: method

Adds a debug marker string to a specific buffer range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+

## Declaration

```swift
func addDebugMarker(_ marker: String, range: Range<Int>)
```

## Parameters

- `marker`: A string that identifies the marked buffer range.
- `range`: The range of bytes that you want to identify.

## See Also

- [func removeAllDebugMarkers()](mtlbuffer/removealldebugmarkers.md)
  Removes all debug marker strings from the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/adddebugmarker(_:range:))*