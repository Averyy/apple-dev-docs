# recurrenceMustBeOnSpecifiedBoundaries

**Framework**: HomeKit  
**Kind**: property

An error indicating the recurrence rule is not on the specified boundaries.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var recurrenceMustBeOnSpecifiedBoundaries: HMError.Code { get }
```

## See Also

- [static var cannotActivateTriggerTooFarInFuture: HMError.Code](hmerror/cannotactivatetriggertoofarinfuture.md)
  An error indicating the trigger cannot be activated because it is set too far in the future.
- [static var dateMustBeOnSpecifiedBoundaries: HMError.Code](hmerror/datemustbeonspecifiedboundaries.md)
  An error indicating the date is not on the specified boundaries.
- [static var fireDateInPast: HMError.Code](hmerror/firedateinpast.md)
  An attempt to activate a timer trigger with a date in the past.
- [static var invalidMessageSize: HMError.Code](hmerror/invalidmessagesize.md)
  An error indicating an invalid message size.
- [static var maximumObjectLimitReached: HMError.Code](hmerror/maximumobjectlimitreached.md)
  An error indicating the maximum object count has been reached.
- [static var recurrenceTooLarge: HMError.Code](hmerror/recurrencetoolarge.md)
  An attempt to use a recurrence period that is too large.
- [static var recurrenceTooSmall: HMError.Code](hmerror/recurrencetoosmall.md)
  An error indicating the recurrence interval is too short.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/recurrencemustbeonspecifiedboundaries)*