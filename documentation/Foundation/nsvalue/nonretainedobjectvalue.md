# nonretainedObjectValue

**Framework**: Foundation  
**Kind**: property

The value as a non-retained pointer to an object.

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
var nonretainedObjectValue: Any? { get }
```

#### Discussion

If the value was not created to hold a pointer-sized data item, the result is undefined.

## See Also

- [init(pointer: UnsafeRawPointer?)](nsvalue/init(pointer:).md)
  Creates a value object containing the specified pointer.
- [init(nonretainedObject: Any?)](nsvalue/init(nonretainedobject:).md)
  Creates a value object containing the specified object.
- [var pointerValue: UnsafeMutableRawPointer?](nsvalue/pointervalue.md)
  Returns the value as an untyped pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/nonretainedobjectvalue)*