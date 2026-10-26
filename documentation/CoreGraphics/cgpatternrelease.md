# CGPatternRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a Core Graphics pattern.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGPatternRelease(CGPatternRef pattern);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `pattern` parameteris `NULL`.

## Parameters

- `pattern`: The pattern to release.

## See Also

### Retaining and Releasing a Pattern
- [CGPatternRetain](./cgpatternretain.md)
  Increments the retain count of a Core Graphics pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatternrelease)*