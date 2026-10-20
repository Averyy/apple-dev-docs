# mount(options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 27.0+

## Declaration

```swift
func mount(options: FSTaskOptions, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func mount(options: FSTaskOptions) async throws
```

```objc
- (void) mountWithOptions:(FSTaskOptions *) options replyHandler:(void (^)(NSError *error)) reply;
```

## See Also

### Mounting and unmounting
- [func unmount(replyHandler: () -> Void)](./unmount%28replyhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/mount(options:replyhandler:))*