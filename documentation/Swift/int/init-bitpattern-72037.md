# init(bitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the same memory representation as the given value.

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
init(bitPattern x: UInt)
```

#### Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.

## Parameters

- `x`: A value to use as the source of the new instance’s binary   representation.

## See Also

- [init<T>(T)](int/init(_:)-4ekvl.md)
  Creates a new instance from the given integer.
- [init?<T>(exactly: T)](int/init(exactly:)-b1dy.md)
- [init<Other>(clamping: Other)](int/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init?(exactly: NSNumber)](int/init(exactly:)-177ax.md)
- [init(truncating: NSNumber)](int/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(bitpattern:)-72037)*