# HKReferenceSex

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
enum HKReferenceSex
```

```c
enum HKReferenceSex : NSInteger;
```

## Overview

The sex whose reference ranges should be used when classifying a clinical measurement for the user.

Distinct from HKBiologicalSex, which represents the user’s biological sex as shown in their Health profile. Use HKReferenceSex when choosing which reference range applies, and HKBiologicalSex when displaying or reasoning about the profile value itself. The two are independent and may differ.

## Topics

### Enumeration Cases
- [HKReferenceSex.female](./hkreferencesex/female.md)
- [HKReferenceSex.male](./hkreferencesex/male.md)
- [HKReferenceSex.notSet](./hkreferencesex/notset.md)
### Initializers
- [init?(rawValue: Int)](./hkreferencesex/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkreferencesex)*