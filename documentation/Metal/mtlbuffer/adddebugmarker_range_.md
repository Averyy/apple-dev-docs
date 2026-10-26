# addDebugMarker:range:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Adds a debug marker string to a specific buffer range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
- (void) addDebugMarker:(NSString *) marker range:(NSRange) range;
```

## Parameters

- `marker`: A string that identifies the marked buffer range.
- `range`: The range of bytes that you want to identify.

## See Also

### Debugging buffers
- [func removeAllDebugMarkers()](./removealldebugmarkers%28%29.md)
  Removes all debug marker strings from the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/adddebugmarker:range:)*