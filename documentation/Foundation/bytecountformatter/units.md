# ByteCountFormatter.Units

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSByteCountFormatterUnits : NSUInteger;
```

## Topics

### Constants
- [static var useBytes: ByteCountFormatter.Units](./units/usebytes.md)
  Displays bytes in the formatter content.
- [static var useKB: ByteCountFormatter.Units](./units/usekb.md)
  Displays kilobytes in the formatter content.
- [static var useMB: ByteCountFormatter.Units](./units/usemb.md)
  Displays megabytes in the formatter content.
- [static var useGB: ByteCountFormatter.Units](./units/usegb.md)
  Displays gigabytes in the formatter content.
- [static var useTB: ByteCountFormatter.Units](./units/usetb.md)
  Displays terabytes in the formatter content.
- [static var usePB: ByteCountFormatter.Units](./units/usepb.md)
  Displays petabyte in the formatter content.
- [static var useEB: ByteCountFormatter.Units](./units/useeb.md)
  Displays exabytes in the formatter content.
- [static var useZB: ByteCountFormatter.Units](./units/usezb.md)
  Displays zettabytes in the formatter content.
- [static var useYBOrHigher: ByteCountFormatter.Units](./units/useyborhigher.md)
  Displays yottabytes in the formatter content.
- [static var useAll: ByteCountFormatter.Units](./units/useall.md)
  Can use any unit in the formatter content.
### Initializers
- [init(rawValue: UInt)](./units/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [ByteCountFormatter.CountStyle](./countstyle-swift.enum.md)
  Specifies display of file or storage byte counts. The display style is platform specific.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/units)*