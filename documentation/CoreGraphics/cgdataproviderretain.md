# CGDataProviderRetain

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Increments the retain count of a data provider.

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
extern CGDataProviderRefCGDataProviderRetain(CGDataProviderRef provider);
```

#### Return Value

The same data provider you passed in as the `provider` parameter.

#### Discussion

This function is equivalent to [`CFRetain`](../CoreFoundation/cfretain.md), except that it does not cause an error if the `provider` parameter is `NULL`.

## Parameters

- `provider`: The data provider to retain.

## See Also

### Retaining and Releasing Data Providers
- [CGDataProviderRelease](./cgdataproviderrelease.md)
  Decrements the retain count of a data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderretain)*