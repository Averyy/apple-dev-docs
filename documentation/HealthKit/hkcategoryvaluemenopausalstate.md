# HKCategoryValueMenopausalState

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

A value that indicates the menopausal state at a recorded point in time.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum HKCategoryValueMenopausalState
```

```c
enum HKCategoryValueMenopausalState : NSInteger;
```

## Mentions

- [Recording and querying menopausal state](./recording-and-querying-menopausal-state.md)

## Overview

Use these values when creating [`HKCategorySample`](./hkcategorysample.md) instances with the [`menopausalState`](./hkcategorytypeidentifier/menopausalstate.md) type. Each value records a person’s menopausal state at a specific date. Apps can query multiple samples over time to derive higher-level interpretations such as active periods, transitions, or current state.

## Topics

### Specifying a menopausal state value
- [HKCategoryValueMenopausalState.menopause](./hkcategoryvaluemenopausalstate/menopause.md)
  A value that indicates the person is in menopause at the sample date.
- [HKCategoryValueMenopausalState.perimenopause](./hkcategoryvaluemenopausalstate/perimenopause.md)
  A value that indicates the person is in perimenopause at the sample date.
- [HKCategoryValueMenopausalState.none](./hkcategoryvaluemenopausalstate/none.md)
  A value that indicates no menopausal state applies at the sample date.
### Creating a value
- [init?(rawValue: Int)](./hkcategoryvaluemenopausalstate/init%28rawvalue%29.md)
  Initializes information about menopausal state.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [HKCategoryValuePredicateProviding](./hkcategoryvaluepredicateproviding.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Menopause
- [Recording and querying menopausal state](./recording-and-querying-menopausal-state.md)
  Personalize someone’s experience on a health app by tracking the information they record on menopausal state.
- [static let menopausalState: HKCategoryTypeIdentifier](./hkcategorytypeidentifier/menopausalstate.md)
  An identifier for samples that record a person’s menopausal state.
- [static let bleedingAfterMenopause: HKCategoryTypeIdentifier](./hkcategorytypeidentifier/bleedingaftermenopause.md)
  An identifier for samples that record bleeding after menopause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenopausalstate)*