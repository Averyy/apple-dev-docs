# init(exactly:)

**Framework**: Swift  
**Kind**: init

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## See Also

- [init<T>(T)](int/init(_:)-4ekvl.md)
  Creates a new instance from the given integer.
- [init<Other>(clamping: Other)](int/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern: UInt)](int/init(bitpattern:)-72037.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](int/init(exactly:)-177ax.md)
- [init(truncating: NSNumber)](int/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(exactly:)-b1dy)*