# notify_register_file_descriptor(_:_:_:_:)

**Framework**: Darwin Notify  
**Kind**: func

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func notify_register_file_descriptor(_ name: UnsafePointer<CChar>!, _ notify_fd: UnsafeMutablePointer<Int32>!, _ flags: Int32, _ out_token: UnsafeMutablePointer<Int32>!) -> UInt32
```

## See Also

- [func notify_is_valid_token(Int32) -> Bool](notify_is_valid_token(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/notify_register_file_descriptor(_:_:_:_:))*