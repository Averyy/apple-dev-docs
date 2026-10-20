# kCMMemoryPoolOption_AgeOutPeriod

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

The period of time before the pool recycles its memory.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMMemoryPoolOption_AgeOutPeriod: CFString
```

```c
extern CFStringRef const kCMMemoryPoolOption_AgeOutPeriod;
```

#### Discussion

Pass a value for this option to the [`CMMemoryPoolCreate(options:)`](./cmmemorypoolcreate%28options%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmmemorypooloption_ageoutperiod)*