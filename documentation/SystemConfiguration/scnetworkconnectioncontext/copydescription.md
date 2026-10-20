# copyDescription

**Framework**: System Configuration  
**Kind**: property  
**Role**: Instance Property

The callback used to provide a description of the `info` field.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?
```

```c
const struct __CFString *(*)(const void *) copyDescription;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext/copydescription)*