# nanoseconds(_:)

**Framework**: Swift  
**Kind**: method

Construct a `Duration` given a number of nanoseconds represented as a `BinaryInteger`.

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
static func nanoseconds<T>(_ nanoseconds: T) -> Duration where T : BinaryInteger
```

#### Return Value

A `Duration` representing a given number of nanoseconds.

#### Discussion

```swift
  let d: Duration = .nanoseconds(1929)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/nanoseconds(_:)-8nsaz)*