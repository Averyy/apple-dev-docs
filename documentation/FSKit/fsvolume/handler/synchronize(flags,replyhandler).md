# synchronize(flags:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 27.0+

## Declaration

```swift
func synchronize(flags: FSSyncFlags, replyHandler reply: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func synchronize(flags: FSSyncFlags) async throws
```

```objc
- (void) synchronizeWithFlags:(FSSyncFlags) flags replyHandler:(void (^)(NSError *error)) reply;
```

## See Also

### Performing synchronization
- [enum FSSyncFlags](../../fssyncflags.md)
  Behavior flags for use with synchronization calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/synchronize(flags:replyhandler:))*