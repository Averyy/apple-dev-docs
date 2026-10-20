# GLKMatrix2

**Framework**: GLKit  
**Kind**: typealias  
**Role**: Type Alias

A `2x2` matrix.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
typealias GLKMatrix2 = _GLKMatrix2
```

```c
typedef union _GLKMatrix2 GLKMatrix2;
```

##### Fields

| Name | Description |
| --- | --- |
| `m` | A one-dimensional array of the matrix’s elements in column-major order. |
| `m00` | The `[0,0]` element of the matrix. |
| `m10` | The `[1,0]` element of the matrix. |
| `m11` | The `[1,1]` element of the matrix. |
| `m2` | A two-dimensional array of the matrix’s elements in column-major order. |

## See Also

### Data Types
- [typealias GLKMatrix3](./glkmatrix3.md)
  A `3x3` matrix stored in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmatrix2)*