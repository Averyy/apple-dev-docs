# maximumConcurrentCompilationTaskCount

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The maximum number of concurrent compilation tasks the device is running.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.3+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maximumConcurrentCompilationTaskCount: Int { get }
```

#### Discussion

The property’s value can change when you set the [`shouldMaximizeConcurrentCompilation`](mtldevice/shouldmaximizeconcurrentcompilation.md) property to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maximumconcurrentcompilationtaskcount)*