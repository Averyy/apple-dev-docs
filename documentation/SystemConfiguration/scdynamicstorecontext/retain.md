# retain

**Framework**: System Configuration  
**Kind**: property  
**Role**: Instance Property

The callback used to add a retain for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value of this parameter can be `NULL`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?
```

```c
const void *(*)(const void *) retain;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/retain)*