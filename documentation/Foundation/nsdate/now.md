# now

**Framework**: Foundation  
**Kind**: property

The current date and time, as of the time of access.

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
class var now: Date { get }
```

#### Discussion

This is equivalent to initializing a new instance with `NSDate()` (or `[[NSDate alloc] init]` in Objective-C). The [`NSDate`](nsdate.md) instance doesn’t automatically update its time after you retrieve it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/now)*