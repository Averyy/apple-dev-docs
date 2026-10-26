# CGDataConsumerRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a data consumer.

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
extern CGDataConsumerRefCGDataConsumerRetain(CGDataConsumerRef consumer);
```

#### Return Value

The same data consumer you passed in as the `consumer` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `consumer` parameter is `NULL`.

## Parameters

- `consumer`: The data consumer to retain.

## See Also

### Retaining and Releasing Data Consumers
- [CGDataConsumerRelease](./cgdataconsumerrelease.md)
  Decrements the retain count of a data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerretain)*