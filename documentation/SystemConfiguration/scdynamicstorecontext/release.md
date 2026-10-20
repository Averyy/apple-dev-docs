# release

**Framework**: System Configuration  
**Kind**: property  
**Role**: Instance Property

The callback used to remove a retain previously added for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value of this parameter can be `NULL`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var release: ((UnsafeRawPointer) -> Void)?
```

```c
void (*)(const void *) release;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/release)*