# cpuOnly

**Framework**: Core AI  
**Kind**: property

Options that restrict compute to the CPU only.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let cpuOnly: SpecializationOptions
```

#### Discussion

The resulting specialized model only uses the CPU during inference. Because all operations support the CPU, no fallback to other compute units occurs.

## See Also

- [static let `default`: SpecializationOptions](specializationoptions/default.md)
  Options that allow the model to use all available compute units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions/cpuonly)*