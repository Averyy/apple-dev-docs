# NSGetSizeAndAlignment(_:_:_:)

**Framework**: Foundation  
**Kind**: func

Obtains the actual size and the aligned size of an encoded type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSGetSizeAndAlignment(_ typePtr: UnsafePointer<CChar>, _ sizep: UnsafeMutablePointer<Int>?, _ alignp: UnsafeMutablePointer<Int>?) -> UnsafePointer<CChar>
```

#### Discussion

Obtains the actual size and the aligned size of the first data type represented by `typePtr` and returns a pointer to the position of the next data type in `typePtr`. You can specify `NULL` for either `sizep` or `alignp` to ignore the corresponding information.

The value returned in `alignp` is the aligned size of the data type; for example, on some platforms, the aligned size of a `char` might be 2 bytes while the actual physical size is 1 byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgetsizeandalignment(_:_:_:))*