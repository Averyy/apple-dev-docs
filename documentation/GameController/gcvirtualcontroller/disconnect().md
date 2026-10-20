# disconnect()

**Framework**: Game Controller  
**Kind**: method

Disconnects the virtual controller from the device and removes it from the screen.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func disconnect()
```

#### Discussion

After you invoke this method, the framework stops calling input handlers that you set for the elements.

## See Also

- [func connect(replyHandler: (((any Error)?) -> Void)?)](gcvirtualcontroller/connect(replyhandler:).md)
  Connects the virtual controller to the device and displays it on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/disconnect())*