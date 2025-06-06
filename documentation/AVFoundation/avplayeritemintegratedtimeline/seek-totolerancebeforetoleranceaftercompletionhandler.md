# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Seeks to a particular time in the integrated time domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

## Parameters

- `time`: A time represented in the integrated time domain.
- `toleranceBefore`: A tolerance before the target time to allow.
- `toleranceAfter`: A tolerance after the target time to allow.
- `completionHandler`: A callback the system invokes after the seek completes. It passes a Boolean value of   if the playhead moved to the new time.

## See Also

- [func seek(to: Date, completionHandler: ((Bool) -> Void)?)](avplayeritemintegratedtimeline/seek(to:completionhandler:).md)
  Seeks to a particular date in the integrated time domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/seek(to:tolerancebefore:toleranceafter:completionhandler:))*