# retain

**Framework**: System Configuration  
**Kind**: property

The callback used to add a retain for the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value of this parameter can be `NULL`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecontext/retain)*