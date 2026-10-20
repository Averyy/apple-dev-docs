# usesCPUOnly

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a prediction is computed using only the CPU.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.13+ - Deprecated in 12.0
- tvOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

## Declaration

```swift
var usesCPUOnly: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL usesCPUOnly;
```

#### Discussion

Your model should be restricted to the CPU if it might run in the background or if your app has other GPU intensive tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlpredictionoptions/usescpuonly)*