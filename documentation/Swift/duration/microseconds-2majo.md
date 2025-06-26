# microseconds(_:)

**Framework**: Swift  
**Kind**: method

Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func microseconds<T>(_ microseconds: T) -> Duration where T : BinaryInteger
```

#### Return Value

A `Duration` representing a given number of microseconds.

#### Discussion

```swift
  let d: Duration = .microseconds(12)
```

## See Also

- [init(secondsComponent: Int64, attosecondsComponent: Int64)](duration/init(secondscomponent:attosecondscomponent:).md)
  Construct a `Duration` by adding attoseconds to a seconds value.
- [static func seconds<T>(T) -> Duration](duration/seconds(_:)-311cx.md)
  Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [static func seconds(Double) -> Duration](duration/seconds(_:)-5ifzr.md)
  Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [static func milliseconds<T>(T) -> Duration](duration/milliseconds(_:)-1w328.md)
  Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [static func milliseconds(Double) -> Duration](duration/milliseconds(_:)-7ledy.md)
  Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [static func microseconds(Double) -> Duration](duration/microseconds(_:)-1zzcc.md)
  Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/microseconds(_:)-2majo)*