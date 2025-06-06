# view(_:shouldRenderAtTime:)

**Framework**: SpriteKit  
**Kind**: method

Specifies whether the view should render at the given time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func view(_ view: SKView, shouldRenderAtTime time: TimeInterval) -> Bool
```

#### Return Value

Return `true` to initiate an update and render for the target time. Return `false` to skip the update and render for the target time.

## Parameters

- `view`: The SKView.
- `time`: The target time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skviewdelegate/view(_:shouldrenderattime:))*