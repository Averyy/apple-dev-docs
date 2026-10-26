# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Stores a sample value at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(NSNumber *) value atIndexedSubscript:(NSUInteger) index;
```

#### Discussion

The method converts the value to a single precision floating-point value. If the index you specified is out of bounds, this method does nothing.

## Parameters

- `value`: The new value to set.
- `index`: The index of the element you want to set.

## See Also

### Accessing the array
- [- objectAtIndexedSubscript:](./objectatindexedsubscript_.md)
  Retrieves the sample value at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray/setobject:atindexedsubscript:)*