# timestamp

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The time when the event occurred.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

#### Discussion

This property contains the number of seconds that have elapsed since system startup. For a description of this time value, see the description of the [`systemUptime`](../../Foundation/processinfo/systemuptime.md) method of the [`ProcessInfo`](../../Foundation/processinfo.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/timestamp)*