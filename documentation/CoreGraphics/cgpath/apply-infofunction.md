# apply(info:function:)

**Framework**: Core Graphics  
**Kind**: method

For each element in a graphics path, calls a custom applier function.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)
```

#### Discussion

For each element in the specified path, Core Graphics calls the applier function, which can examine (but not modify) the element.

## Parameters

- `info`: A pointer to the user data that Core Graphics will pass to the function being applied, or  .
- `function`: A pointer to the function to apply. See   for more information.

## See Also

- [typealias CGPathApplierFunction](cgpathapplierfunction.md)
  Defines a callback function that can view an element in a graphics path.
- [struct CGPathElement](cgpathelement.md)
  A data structure that provides information about a path element.
- [enum CGPathElementType](cgpathelementtype.md)
  The type of element found in a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/apply(info:function:))*