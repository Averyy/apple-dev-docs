# FileDescriptor.SeekOrigin.RawValue

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

- [init(rawValue: CInt)](filedescriptor/seekorigin/init(rawvalue:).md)
  Create a strongly-typed seek origin from a raw C value.
- [var rawValue: CInt](filedescriptor/seekorigin/rawvalue-swift.property.md)
  The raw C value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seekorigin/rawvalue-swift.typealias)*