# shouldMaximizeConcurrentCompilation

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the device uses additional CPU threads for compilation tasks.

**Availability**:
- macOS 13.3+

## Declaration

```swift
var shouldMaximizeConcurrentCompilation: Bool { get set }
```

## Mentions

- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)

#### Discussion

The property’s default value is [`false`](https://developer.apple.com/documentation/Swift/false). You can retrieve the number of concurrent CPU threads the device is currently using by checking the [`maximumConcurrentCompilationTaskCount`](mtldevice/maximumconcurrentcompilationtaskcount.md) property.

> **Note**: The number of additional CPU threads automatically scales with the system’s hardware capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/shouldmaximizeconcurrentcompilation)*