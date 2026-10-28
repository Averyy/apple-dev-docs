# CGPatternRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a Core Graphics pattern.

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
extern CGPatternRefCGPatternRetain(CGPatternRef pattern);
```

## Return Value

The same pattern youpassed in as the `pattern` parameter.

## Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md),except that it does not cause an error if the `pattern` parameteris `NULL`.

## Parameters

- `pattern`: The pattern to retain.

## See Also

### Retaining and Releasing a Pattern
- [CGPatternRelease](./cgpatternrelease.md)
  Decrements the retain count of a Core Graphics pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpatternretain)*