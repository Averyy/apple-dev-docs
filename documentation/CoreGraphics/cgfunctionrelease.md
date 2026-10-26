# CGFunctionRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a function object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGFunctionRelease(CGFunctionRef function);
```

#### Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `function` parameter is `nil`.

## Parameters

- `function`: The function object to release.

## See Also

### Retaining and Releasing CGFunction Objects
- [CGFunctionRetain](./cgfunctionretain.md)
  Increments the retain count of a function object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctionrelease)*