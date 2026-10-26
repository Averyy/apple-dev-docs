# NSTextAlignmentToCTTextAlignment

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern CTTextAlignment NSTextAlignmentToCTTextAlignment(NSTextAlignment nsTextAlignment);
```

#### Return Value

The Core Text alignment that corresponds to the value specified in `nsTextAlignment`.

#### Discussion

Use this function when you need to map between the UIKit and Core Text constants for text alignment.

## Parameters

- `nsTextAlignment`: The UIKit text alignment constant you want to convert.

## See Also

### Text manipulations
- [init(CTTextAlignment)](./nstextalignment/init%28_%29.md)
  Converts a Core Text alignment constant value to the matching constant value in UIKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextalignmenttocttextalignment)*