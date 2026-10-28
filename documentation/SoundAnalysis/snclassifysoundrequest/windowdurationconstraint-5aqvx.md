# windowDurationConstraint

**Framework**: Sound Analysis  
**Kind**: property  
**Role**: Instance Property

A range or list of sound duration times the request’s underlying sound classifier supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (strong, readonly) SNTimeDurationConstraint * windowDurationConstraint;
```

## Discussion

Configure the request’s [`windowDuration`](./windowduration.md) property with a value that satisfies the window duration constraint.

## See Also

### Instance Properties
- [SNTimeDurationConstraint](../sntimedurationconstraint-c.class.md)
  Defines the time duration windows the request’s underlying sound classifier accepts with a range, or an array, of durations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest/windowdurationconstraint-5aqvx)*