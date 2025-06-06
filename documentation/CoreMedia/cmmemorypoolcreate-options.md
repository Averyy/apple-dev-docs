# CMMemoryPoolCreate(options:)

**Framework**: Core Media  
**Kind**: func

Creates a memory pool.

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
func CMMemoryPoolCreate(options: CFDictionary?) -> CMMemoryPool
```

#### Return Value

A new memory pool.

## Parameters

- `options`: A dictionary that defines the age-out period for the pool.

## Topics

### Creation Options
- [let kCMMemoryPoolOption_AgeOutPeriod: CFString](kcmmemorypooloption_ageoutperiod.md)
  The period of time before the pool recycles its memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmemorypoolcreate(options:))*