# setObject:forKeyedSubscript:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Assigns a number to the multiarray’s element at the location that the number array defines.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
- (void) setObject:(NSNumber *) obj forKeyedSubscript:(NSArray<NSNumber *> *) key;
```

## Discussion

See [`subscript(_:)`](./subscript%28_%29-3d9el.md) for the method’s getter counterpart.

## Parameters

- `obj`: An [`NSNumber`](../../Foundation/nsnumber.md) to assign to the element.
- `key`: An [`NSNumber`](../../Foundation/nsnumber.md) array that represents an element’s position in the multiarray. Each element of `key` is an index into the multiarray’s corresponding dimension.

## See Also

### Accessing a multiarray’s elements
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the linear offset defines.
- [- getBytesWithHandler:](./getbyteswithhandler_.md)
  Get the underlying buffer pointer to read.
- [- getMutableBytesWithHandler:](./getmutablebyteswithhandler_.md)
  Get the underlying buffer pointer to mutate.
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.
- [var dataPointer: UnsafeMutableRawPointer](./datapointer.md)
  A pointer to the multiarray’s underlying memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/setobject:forkeyedsubscript:)*