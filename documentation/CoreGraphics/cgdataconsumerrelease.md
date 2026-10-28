# CGDataConsumerRelease

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Decrements the retain count of a data consumer.

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
extern void CGDataConsumerRelease(CGDataConsumerRef consumer);
```

## Discussion

This function is equivalent to [`CFRelease`](../CoreFoundation/cfrelease.md), except that it does not cause an error if the `consumer` parameter is `NULL`.

## Parameters

- `consumer`: The data consumer to release.

## See Also

### Retaining and Releasing Data Consumers
- [CGDataConsumerRetain](./cgdataconsumerretain.md)
  Increments the retain count of a data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerrelease)*