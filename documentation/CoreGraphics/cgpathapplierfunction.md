# CGPathApplierFunction

**Framework**: Core Graphics  
**Kind**: typealias

Defines a callback function that can view an element in a graphics path.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CGPathApplierFunction = (UnsafeMutableRawPointer?, UnsafePointer<CGPathElement>) -> Void
```

#### Discussion

See also [`apply(info:function:)`](cgpath/apply(info:function:).md).

## See Also

- [func apply(info: UnsafeMutableRawPointer?, function: CGPathApplierFunction)](cgpath/apply(info:function:).md)
  For each element in a graphics path, calls a custom applier function.
- [struct CGPathElement](cgpathelement.md)
  A data structure that provides information about a path element.
- [enum CGPathElementType](cgpathelementtype.md)
  The type of element found in a path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathapplierfunction)*