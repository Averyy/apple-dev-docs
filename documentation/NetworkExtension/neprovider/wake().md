# wake()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Handle a wake event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func wake()
```

```objc
- (void) wake;
```

#### Discussion

This method is called by the system when the device wakes up from sleep mode.

`NEProvider` subclasses should override this method if the provider needs to perform any tasks when the device wakes up, such as reconnecting a tunnel connection.

## See Also

### Handling sleep and wake
- [func sleep(completionHandler: () -> Void)](./sleep%28completionhandler%29.md)
  Handle a sleep event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/wake())*