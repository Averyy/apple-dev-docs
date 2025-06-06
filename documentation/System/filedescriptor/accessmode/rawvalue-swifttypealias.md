# FileDescriptor.AccessMode.RawValue

**Framework**: System  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
typealias RawValue = CInt
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [init(rawValue: CInt)](filedescriptor/accessmode/init(rawvalue:).md)
  Creates a strongly-typed access mode from a raw C access mode.
- [var rawValue: CInt](filedescriptor/accessmode/rawvalue-swift.property.md)
  The raw C access mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode/rawvalue-swift.typealias)*