# MTLForwardProgressUsage.automatic

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Instructs the Metal compiler to decide which forward progress mode to apply to the pipeline by analyzing its program.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case automatic
```

```c
MTLForwardProgressUsageAutomatic
```

## Discussion

The implementation uses a conservative detection scheme. Select a specific setting if the default detection is insufficient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlforwardprogressusage/automatic)*