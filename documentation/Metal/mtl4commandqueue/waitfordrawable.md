# waitForDrawable(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules a wait operation on the command queue to ensure the display is no longer using a specific Metal drawable.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func waitForDrawable(_ drawable: any MTLDrawable)
```

#### Discussion

Use this method to ensure the display is no longer using a [`MTLDrawable`](mtldrawable.md) instance before executing any subsequent commands.

This method returns immediately and doesn’t perform any synchronization on the current thread. You are responsible for calling this method before committing any command buffers containing commands that target this drawable.

Call this method multiple times if you commit your command buffers to multiple command queues.

## Parameters

- `drawable`:   instance to signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/waitfordrawable(_:))*