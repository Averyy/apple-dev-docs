# allComputeDevices

**Framework**: Core ML  
**Kind**: property

Returns an array that contains all of the compute devices that are accessible.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var allComputeDevices: [MLComputeDevice] { get }
```

#### Discussion

If a compute device becomes inaccessible, this array won’t include it. For example, this array won’t contain the GPU device after it’s removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputedevice/allcomputedevices)*