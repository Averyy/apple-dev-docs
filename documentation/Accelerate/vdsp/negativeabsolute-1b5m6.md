# negativeAbsolute(_:)

**Framework**: Accelerate  
**Kind**: method

Returns the negative absolute value of each element in the supplied double-precision vector.

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
static func negativeAbsolute<U>(_ vector: U) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

For example, the following code calculates the negative absolute values of the elements of an array:

```swift
    let values: [Double] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let negativeAbsoluteValues = vDSP.negativeAbsolute(values)
    
    // Prints "[-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0]".
    print(negativeAbsoluteValues)
```

## Parameters

- `vector`: The source vector.

## See Also

- [static func negativeAbsolute<U>(U) -> [Float]](vdsp/negativeabsolute(_:)-66a7a.md)
  Returns the negative absolute value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](vdsp/negativeabsolute(_:result:)-85gj0.md)
  Calculates the negative absolute value of each element in the supplied single-precision vector.
- [static func negativeAbsolute<U, V>(U, result: inout V)](vdsp/negativeabsolute(_:result:)-1gpcy.md)
  Calculates the negative absolute value of each element in the supplied double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/negativeabsolute(_:)-1b5m6)*