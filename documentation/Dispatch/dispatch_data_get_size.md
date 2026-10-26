# dispatch_data_get_size

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Returns the logical size of the memory managed by a dispatch data object

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern size_t dispatch_data_get_size(dispatch_data_t data);
```

#### Return Value

The number of bytes represented by the data object.

#### Discussion

For data objects that represent multiple noncontiguous memory regions, the size reported by this function is the sum of the sizes of the individual regions.

## Parameters

- `data`: The dispatch data object to query


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_data_get_size)*