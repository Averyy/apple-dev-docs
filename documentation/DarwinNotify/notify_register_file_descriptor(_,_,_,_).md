# notify_register_file_descriptor(_:_:_:_:)

**Framework**: Darwin Notify  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func notify_register_file_descriptor(_ name: UnsafePointer<CChar>!, _ notify_fd: UnsafeMutablePointer<Int32>!, _ flags: Int32, _ out_token: UnsafeMutablePointer<Int32>!) -> UInt32
```

```c
extern uint32_t notify_register_file_descriptor(const char *name, int *notify_fd, int flags, int *out_token);
```

## See Also

### Functions
- [func notify_is_valid_token(Int32) -> Bool](./notify_is_valid_token%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_file_descriptor(_:_:_:_:))*