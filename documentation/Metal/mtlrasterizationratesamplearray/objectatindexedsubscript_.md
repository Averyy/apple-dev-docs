# objectAtIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Retrieves the sample value at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (NSNumber *) objectAtIndexedSubscript:(NSUInteger) index;
```

#### Return Value

An [`NSNumber`](../../Foundation/nsnumber.md) object. It contains the value of the sample at the specified index or `0` if the index you specified is out of bounds.

## Parameters

- `index`: The index of the element to retrieve.

## See Also

### Accessing the array
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Stores a sample value at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray/objectatindexedsubscript:)*