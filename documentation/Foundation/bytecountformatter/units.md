# ByteCountFormatter.Units

**Framework**: Foundation  
**Kind**: struct

Specifies the units appropriate for the formatter to display. Specifying any units explicitly causes just those units to be used in showing the number.

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
struct Units
```

## Topics

### Constants
- [static var useBytes: ByteCountFormatter.Units](bytecountformatter/units/usebytes.md)
  Displays bytes in the formatter content.
- [static var useKB: ByteCountFormatter.Units](bytecountformatter/units/usekb.md)
  Displays kilobytes in the formatter content.
- [static var useMB: ByteCountFormatter.Units](bytecountformatter/units/usemb.md)
  Displays megabytes in the formatter content.
- [static var useGB: ByteCountFormatter.Units](bytecountformatter/units/usegb.md)
  Displays gigabytes in the formatter content.
- [static var useTB: ByteCountFormatter.Units](bytecountformatter/units/usetb.md)
  Displays terabytes in the formatter content.
- [static var usePB: ByteCountFormatter.Units](bytecountformatter/units/usepb.md)
  Displays petabyte in the formatter content.
- [static var useEB: ByteCountFormatter.Units](bytecountformatter/units/useeb.md)
  Displays exabytes in the formatter content.
- [static var useZB: ByteCountFormatter.Units](bytecountformatter/units/usezb.md)
  Displays zettabytes in the formatter content.
- [static var useYBOrHigher: ByteCountFormatter.Units](bytecountformatter/units/useyborhigher.md)
  Displays yottabytes in the formatter content.
- [static var useAll: ByteCountFormatter.Units](bytecountformatter/units/useall.md)
  Can use any unit in the formatter content.
### Initializers
- [init(rawValue: UInt)](bytecountformatter/units/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [ByteCountFormatter.CountStyle](bytecountformatter/countstyle-swift.enum.md)
  Specifies display of file or storage byte counts. The display style is platform specific.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/units)*