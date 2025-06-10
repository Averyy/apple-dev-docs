# sort(_:sortOrder:)

**Framework**: Accelerate  
**Kind**: method

Sorts a vector of single-precision values in-place.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func sort<V>(_ vector: inout V, sortOrder: vDSP.SortOrder) where V : AccelerateMutableBuffer, V.Element == Float
```

#### Discussion

The single- and double-precision [`sort(_:sortOrder:)`](vdsp/sort(_:sortorder:)-wx0w.md) functions sort an array in place.

The following code sorts an array in ascending order, followed by decending order:

```swift
var values: [Float] = [4.0, 8.0, 3.0, 0.0, 7.0, 5.0, 9.0, 2.0, 6.0, 1.0]

vDSP.sort(&values,
          sortOrder: .ascending)

// Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]".
print(values)

vDSP.sort(&values,
          sortOrder: .descending)

// Prints "[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]".
print(values)
```

## Parameters

- `vector`: The array to sort.
- `sortOrder`: The sort order.

## See Also

- [static func sort<V>(inout V, sortOrder: vDSP.SortOrder)](vdsp/sort(_:sortorder:)-418g0.md)
  Sorts a vector of double-precision values in-place.
- [vDSP.SortOrder](vdsp/sortorder.md)
  Constants that specify the sorting order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/sort(_:sortorder:)-wx0w)*