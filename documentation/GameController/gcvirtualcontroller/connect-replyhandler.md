# connect(replyHandler:)

**Framework**: Game Controller  
**Kind**: method

Connects the virtual controller to the device and displays it on the screen.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func connect() async throws
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)

#### Discussion

After you invoke this method, the framework calls any input handlers you set for the elements, or you can poll the elements for their values.

## Parameters

- `reply`: A closure that the method calls upon completion with the following parameter:

## See Also

- [func disconnect()](gcvirtualcontroller/disconnect.md)
  Disconnects the virtual controller from the device and removes it from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/connect(replyhandler:))*