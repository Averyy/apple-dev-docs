# microseconds(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.

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
static func microseconds(_ microseconds: Double) -> Duration
```

## Return Value

A `Duration` representing a given number of microseconds.

## Discussion

```swift
  let d: Duration = .microseconds(382.9)
```

## See Also

### Creating a duration
- [init(secondsComponent: Int64, attosecondsComponent: Int64)](./init%28secondscomponent,attosecondscomponent%29.md)
  Construct a `Duration` by adding attoseconds to a seconds value.
- [static func seconds<T>(T) -> Duration](./seconds%28_%29-311cx.md)
  Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [static func seconds(Double) -> Duration](./seconds%28_%29-5ifzr.md)
  Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [static func milliseconds<T>(T) -> Duration](./milliseconds%28_%29-1w328.md)
  Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [static func milliseconds(Double) -> Duration](./milliseconds%28_%29-7ledy.md)
  Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [static func microseconds<T>(T) -> Duration](./microseconds%28_%29-2majo.md)
  Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/microseconds(_:)-1zzcc)*