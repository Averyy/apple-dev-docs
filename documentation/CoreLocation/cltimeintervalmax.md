# CLTimeIntervalMax

**Framework**: Core Location  
**Kind**: var  
**Role**: Global Variable

A value representing an unlimited amount of time.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CLTimeIntervalMax: TimeInterval
```

```c
extern const NSTimeInterval CLTimeIntervalMax;
```

## Discussion

When scheduling deferred updates, you can use this constant to indicate that a new update should be triggered only after a large time interval has passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cltimeintervalmax)*