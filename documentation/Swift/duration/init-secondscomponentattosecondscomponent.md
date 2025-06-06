# init(secondsComponent:attosecondsComponent:)

**Framework**: Swift  
**Kind**: init

Construct a `Duration` by adding attoseconds to a seconds value.

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
init(secondsComponent: Int64, attosecondsComponent: Int64)
```

#### Discussion

This is useful for when an external decomposed components of a `Duration` has been stored and needs to be reconstituted. Since the values are added no precondition is expressed for the attoseconds being limited to 1e18.

```swift
  let d1 = Duration(
    secondsComponent: 3, 
    attosecondsComponent: 123000000000000000)
  print(d1) // 3.123 seconds

  let d2 = Duration(
    secondsComponent: 3, 
    attosecondsComponent: -123000000000000000)
  print(d2) // 2.877 seconds

  let d3 = Duration(
    secondsComponent: -3, 
    attosecondsComponent: -123000000000000000)
  print(d3) // -3.123 seconds
```

## Parameters

- `secondsComponent`: The seconds component portion of the     value.
- `attosecondsComponent`: The attosecond component portion of the    value.

## See Also

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
- [static func microseconds<T>(T) -> Duration](duration/microseconds(_:)-2majo.md)
  Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.
- [static func nanoseconds<T>(T) -> Duration](duration/nanoseconds(_:).md)
  Construct a `Duration` given a number of nanoseconds represented as a `BinaryInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/init(secondscomponent:attosecondscomponent:))*