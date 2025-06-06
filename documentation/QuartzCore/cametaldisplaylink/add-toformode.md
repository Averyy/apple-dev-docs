# add(to:forMode:)

**Framework**: Core Animation  
**Kind**: method

Registers the display link with a run loop.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func add(to runloop: RunLoop, forMode mode: RunLoop.Mode)
```

#### Discussion

You can associate the display link with any of the [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop) modes, multiple input modes, or a custom mode. When the run loop is in `mode`, the display link notifies its delegate when the system prepares the next frame.

You can remove the display link from a run loop by calling [`remove(from:forMode:)`](cametaldisplaylink/remove(from:formode:).md), or from all run loops with [`invalidate()`](cametaldisplaylink/invalidate().md).

## Parameters

- `runloop`: A run loop instance the method associates with the display link.
- `mode`: A run loop mode for the display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/add(to:formode:))*