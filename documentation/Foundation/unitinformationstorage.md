# UnitInformationStorage

**Framework**: Foundation  
**Kind**: class

A unit of measure for quantities of information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class UnitInformationStorage
```

#### Overview

Use instances of [`UnitInformationStorage`](unitinformationstorage.md) to represent quantities of information using the [`NSMeasurement`](nsmeasurement.md) class. The base unit of measure for information is the bit, with a nibble representing four bits and a byte representing eight bits.

Larger units of information expand on bits and bytes by orders of magnitude in both decimal and binary forms.

##### Information Transfer

Units of bits commonly represent the amount of transferred information.

| Decimal Bits | Coefficient | Binary Bits | Coefficient |
| --- | --- | --- | --- |
| [`kilobits`](unitinformationstorage/kilobits.md) | `1000` | [`kibibits`](unitinformationstorage/kibibits.md) | `1024` |
| [`megabits`](unitinformationstorage/megabits.md) | `1000e2` | [`mebibits`](unitinformationstorage/mebibits.md) | `1024e2` |
| [`gigabits`](unitinformationstorage/gigabits.md) | `1000e3` | [`gibibits`](unitinformationstorage/gibibits.md) | `1024e3` |
| [`terabits`](unitinformationstorage/terabits.md) | `1000e4` | [`tebibits`](unitinformationstorage/tebibits.md) | `1024e4` |
| [`petabits`](unitinformationstorage/petabits.md) | `1000e5` | [`pebibits`](unitinformationstorage/pebibits.md) | `1024e5` |
| [`exabits`](unitinformationstorage/exabits.md) | `1000e6` | [`exbibits`](unitinformationstorage/exbibits.md) | `1024e6` |
| [`zettabits`](unitinformationstorage/zettabits.md) | `1000e7` | [`zebibits`](unitinformationstorage/zebibits.md) | `1024e7` |
| [`yottabits`](unitinformationstorage/yottabits.md) | `1000e8` | [`yobibits`](unitinformationstorage/yobibits.md) | `1024e8` |

##### Information Storage

Units of bytes commonly represent the amount of stored information.

| Decimal Bytes | Coefficient | Binary Bytes | Coefficient |
| --- | --- | --- | --- |
| [`kilobytes`](unitinformationstorage/kilobytes.md) | `1000` | [`kibibytes`](unitinformationstorage/kibibytes.md) | `1024` |
| [`megabytes`](unitinformationstorage/megabytes.md) | `1000e2` | [`mebibytes`](unitinformationstorage/mebibytes.md) | `1024e2` |
| [`gigabytes`](unitinformationstorage/gigabytes.md) | `1000e3` | [`gibibytes`](unitinformationstorage/gibibytes.md) | `1024e3` |
| [`terabytes`](unitinformationstorage/terabytes.md) | `1000e4` | [`tebibytes`](unitinformationstorage/tebibytes.md) | `1024e4` |
| [`petabytes`](unitinformationstorage/petabytes.md) | `1000e5` | [`pebibytes`](unitinformationstorage/pebibytes.md) | `1024e5` |
| [`exabytes`](unitinformationstorage/exabytes.md) | `1000e6` | [`exbibytes`](unitinformationstorage/exbibytes.md) | `1024e6` |
| [`zettabytes`](unitinformationstorage/zettabytes.md) | `1000e7` | [`zebibytes`](unitinformationstorage/zebibytes.md) | `1024e7` |
| [`yottabytes`](unitinformationstorage/yottabytes.md) | `1000e8` | [`yobibytes`](unitinformationstorage/yobibytes.md) | `1024e8` |

## Topics

### Accessing Predefined Common Units
- [class var bits: UnitInformationStorage](unitinformationstorage/bits.md)
  The bits unit of information.
- [class var nibbles: UnitInformationStorage](unitinformationstorage/nibbles.md)
  The nibbles unit of information.
- [class var bytes: UnitInformationStorage](unitinformationstorage/bytes.md)
  The bytes unit of information.
### Accessing Predefined Binary Units
- [class var kibibits: UnitInformationStorage](unitinformationstorage/kibibits.md)
  The kibibits unit of information.
- [class var kibibytes: UnitInformationStorage](unitinformationstorage/kibibytes.md)
  The kibibytes unit of information.
- [class var mebibits: UnitInformationStorage](unitinformationstorage/mebibits.md)
  The mebibits unit of information.
- [class var mebibytes: UnitInformationStorage](unitinformationstorage/mebibytes.md)
  The mebibytes unit of information.
- [class var gibibits: UnitInformationStorage](unitinformationstorage/gibibits.md)
  The gibibits unit of information.
- [class var gibibytes: UnitInformationStorage](unitinformationstorage/gibibytes.md)
  The gibibytes unit of information.
- [class var tebibits: UnitInformationStorage](unitinformationstorage/tebibits.md)
  The tebibits unit of information.
- [class var tebibytes: UnitInformationStorage](unitinformationstorage/tebibytes.md)
  The tebibytes unit of information.
- [class var pebibits: UnitInformationStorage](unitinformationstorage/pebibits.md)
  The pebibits unit of information.
- [class var pebibytes: UnitInformationStorage](unitinformationstorage/pebibytes.md)
  The pebibytes unit of information.
- [class var exbibits: UnitInformationStorage](unitinformationstorage/exbibits.md)
  The exbibits unit of information.
- [class var exbibytes: UnitInformationStorage](unitinformationstorage/exbibytes.md)
  The exbibytes unit of information.
- [class var zebibits: UnitInformationStorage](unitinformationstorage/zebibits.md)
  The zebibits unit of information.
- [class var zebibytes: UnitInformationStorage](unitinformationstorage/zebibytes.md)
  The zebibytes unit of information.
- [class var yobibits: UnitInformationStorage](unitinformationstorage/yobibits.md)
  The yobibits unit of information.
- [class var yobibytes: UnitInformationStorage](unitinformationstorage/yobibytes.md)
  The yobibytes unit of information.
### Accessing Predefined Decimal Units
- [class var kilobits: UnitInformationStorage](unitinformationstorage/kilobits.md)
  The kilobits unit of information.
- [class var kilobytes: UnitInformationStorage](unitinformationstorage/kilobytes.md)
  The kilobytes unit of information.
- [class var megabits: UnitInformationStorage](unitinformationstorage/megabits.md)
  The megabits unit of information.
- [class var megabytes: UnitInformationStorage](unitinformationstorage/megabytes.md)
  The megabytes unit of information.
- [class var gigabits: UnitInformationStorage](unitinformationstorage/gigabits.md)
  The gigabits unit of information.
- [class var gigabytes: UnitInformationStorage](unitinformationstorage/gigabytes.md)
  The gigabytes unit of information.
- [class var terabits: UnitInformationStorage](unitinformationstorage/terabits.md)
  The terabits unit of information.
- [class var terabytes: UnitInformationStorage](unitinformationstorage/terabytes.md)
  The terrabytes unit of information.
- [class var petabits: UnitInformationStorage](unitinformationstorage/petabits.md)
  The petabits unit of information.
- [class var petabytes: UnitInformationStorage](unitinformationstorage/petabytes.md)
  The petabytes unit of information.
- [class var exabits: UnitInformationStorage](unitinformationstorage/exabits.md)
  The exabits unit of information.
- [class var exabytes: UnitInformationStorage](unitinformationstorage/exabytes.md)
  The exabytes unit of information.
- [class var zettabits: UnitInformationStorage](unitinformationstorage/zettabits.md)
  The zettabits unit of information.
- [class var zettabytes: UnitInformationStorage](unitinformationstorage/zettabytes.md)
  The zettabytes unit of information.
- [class var yottabits: UnitInformationStorage](unitinformationstorage/yottabits.md)
  The yottabits unit of information.
- [class var yottabytes: UnitInformationStorage](unitinformationstorage/yottabytes.md)
  The yottabytes unit of information.

## Relationships

### Inherits From
- [Dimension](dimension.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitinformationstorage)*