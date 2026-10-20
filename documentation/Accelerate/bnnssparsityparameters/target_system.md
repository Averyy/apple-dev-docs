# target_system

**Framework**: Accelerate  
**Kind**: property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var target_system: BNNSTargetSystem
```

#### Discussion

Target System values for BNNSGetBestDataLayout* functions

Due to architectural and microarchitectural changes between different types and generations of apple devices, the optimal packing of data varies from device to device. In order to determine the optimal repacking for a given device, the user may call the BNNSGetBestDataLayout* family of functions. These functions take an argument representing the Target System from the values provided by this enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnssparsityparameters/target_system)*