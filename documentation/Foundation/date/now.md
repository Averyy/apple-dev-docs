# now

**Framework**: Foundation  
**Kind**: property

Returns a date instance that represents the current date and time, at the moment of access.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var now: Date { get }
```

#### Discussion

This property is equivalent to calling [`init()`](date/init().md). If you assign this value to a variable or property, the assigned value doesn’t automatically update as time passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/now)*