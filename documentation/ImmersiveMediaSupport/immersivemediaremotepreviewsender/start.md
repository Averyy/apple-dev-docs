# start()

**Framework**: Immersive Media Support  
**Kind**: method

Starts the sender - this needs to be called before starting to send frames, audio or venue descriptor information to receivers. After `start` is called, the application should observe the `isReadyForData` property to know when to start sending frames.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func start() async
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/start())*