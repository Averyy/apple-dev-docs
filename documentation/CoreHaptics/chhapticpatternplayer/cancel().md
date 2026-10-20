# cancel()

**Framework**: Core Haptics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stops the pattern player immediately and returns the specified error.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func cancel() throws
```

```objc
- (BOOL) cancelAndReturnError:(NSError **) outError;
```

## See Also

### Starting and Stopping Playback
- [func start(atTime: TimeInterval) throws](./start%28attime%29.md)
  Starts playing the pattern at the specified time.
- [func stop(atTime: TimeInterval) throws](./stop%28attime%29.md)
  Stops playing the pattern at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer/cancel())*