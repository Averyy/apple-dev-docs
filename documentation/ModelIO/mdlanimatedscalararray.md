# MDLAnimatedScalarArray

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MDLAnimatedScalarArray
```

```objc
@interface MDLAnimatedScalarArray : MDLAnimatedValue
```

## Topics

### Initializers
- [init(elementCount: Int)](./mdlanimatedscalararray/init%28elementcount%29.md)
### Instance Properties
- [var doubleArray: [Double]](./mdlanimatedscalararray/doublearray.md)
- [var elementCount: Int](./mdlanimatedscalararray/elementcount.md)
- [var floatArray: [Float]](./mdlanimatedscalararray/floatarray.md)
### Instance Methods
- [func doubleArray(atTime: TimeInterval) -> [Double]](./mdlanimatedscalararray/doublearray%28attime%29.md)
- [func floatArray(atTime: TimeInterval) -> [Float]](./mdlanimatedscalararray/floatarray%28attime%29.md)
- [func reset(doubleArray: [Double], atTimes: [TimeInterval])](./mdlanimatedscalararray/reset%28doublearray,attimes%29.md)
- [func reset(floatArray: [Float], atTimes: [TimeInterval])](./mdlanimatedscalararray/reset%28floatarray,attimes%29.md)
- [func set(doubleArray: [Double], atTime: TimeInterval)](./mdlanimatedscalararray/set%28doublearray,attime%29.md)
- [func set(floatArray: [Float], atTime: TimeInterval)](./mdlanimatedscalararray/set%28floatarray,attime%29.md)
- [- getDoubleArray:maxCount:](./mdlanimatedscalararray/getdoublearray_maxcount_.md)
- [- getDoubleArray:maxCount:atTime:](./mdlanimatedscalararray/getdoublearray_maxcount_attime_.md)
- [- getFloatArray:maxCount:](./mdlanimatedscalararray/getfloatarray_maxcount_.md)
- [- getFloatArray:maxCount:atTime:](./mdlanimatedscalararray/getfloatarray_maxcount_attime_.md)
- [- resetWithDoubleArray:count:atTimes:count:](./mdlanimatedscalararray/resetwithdoublearray_count_attimes_count_.md)
- [- resetWithFloatArray:count:atTimes:count:](./mdlanimatedscalararray/resetwithfloatarray_count_attimes_count_.md)
- [- setDoubleArray:count:atTime:](./mdlanimatedscalararray/setdoublearray_count_attime_.md)
- [- setFloatArray:count:atTime:](./mdlanimatedscalararray/setfloatarray_count_attime_.md)

## Relationships

### Inherits From
- [MDLAnimatedValue](./mdlanimatedvalue.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedscalararray)*