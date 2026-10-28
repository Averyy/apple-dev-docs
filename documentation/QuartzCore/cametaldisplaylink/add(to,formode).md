# add(to:forMode:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addToRunLoop:(NSRunLoop *) runloop forMode:(NSRunLoopMode) mode;
```

## Discussion

You can associate the display link with any of the [`RunLoop`](../../Foundation/runloop.md) modes, multiple input modes, or a custom mode. When the run loop is in `mode`, the display link notifies its delegate when the system prepares the next frame.

You can remove the display link from a run loop by calling [`remove(from:forMode:)`](./remove%28from,formode%29.md), or from all run loops with [`invalidate()`](./invalidate%28%29.md).

## Parameters

- `runloop`: A run loop instance the method associates with the display link.
- `mode`: A run loop mode for the display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/add(to:formode:))*