# unmount(replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 27.0+

## Declaration

```swift
func unmount(replyHandler reply: @escaping @Sendable () -> Void)
```

```swift
func unmount() async
```

```objc
- (void) unmountWithReplyHandler:(void (^)()) reply;
```

## See Also

### Mounting and unmounting
- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](./mount%28options,replyhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/unmount(replyhandler:))*