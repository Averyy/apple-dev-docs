# now

**Framework**: Foundation  
**Kind**: property

Returns a date instance that represents the current date and time, at the moment of access.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@backDeployed(before: macOS 12, iOS 15, tvOS 15, watchOS 8)
static var now: Date { get }
```

#### Discussion

This property is equivalent to calling [`init()`](date/init().md). If you assign this value to a variable or property, the assigned value doesn’t automatically update as time passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/now)*