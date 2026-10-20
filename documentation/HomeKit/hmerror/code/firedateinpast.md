# HMError.Code.fireDateInPast

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

An attempt to activate a timer trigger with a date in the past.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case fireDateInPast
```

```c
HMErrorCodeFireDateInPast
```

## See Also

### Limit errors
- [HMError.Code.cannotActivateTriggerTooFarInFuture](./cannotactivatetriggertoofarinfuture.md)
  An error indicating the trigger cannot be activated because it is set too far in the future.
- [HMError.Code.dateMustBeOnSpecifiedBoundaries](./datemustbeonspecifiedboundaries.md)
  An error indicating the date is not on the specified boundaries.
- [HMError.Code.invalidMessageSize](./invalidmessagesize.md)
  An error indicating an invalid message size.
- [HMError.Code.maximumObjectLimitReached](./maximumobjectlimitreached.md)
  An error indicating the maximum object count has been reached.
- [HMError.Code.recurrenceTooLarge](./recurrencetoolarge.md)
  An attempt to use a recurrence period that is too large.
- [HMError.Code.recurrenceTooSmall](./recurrencetoosmall.md)
  An error indicating the recurrence interval is too short.
- [HMError.Code.recurrenceMustBeOnSpecifiedBoundaries](./recurrencemustbeonspecifiedboundaries.md)
  An error indicating the recurrence rule is not on the specified boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code/firedateinpast)*