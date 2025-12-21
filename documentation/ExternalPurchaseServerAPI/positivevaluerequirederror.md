# PositiveValueRequiredError

**Framework**: External Purchase Server API  
**Kind**: dictionary

An error indicating the field requires a positive value.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object PositiveValueRequiredError
```

## See Also

- [object DateTooFarInPastError](datetoofarinpasterror.md)
  An error indicating that a provided date is too far in the past.
- [object DuplicateTokenStatusNotAllowedError](duplicatetokenstatusnotallowederror.md)
  An error indicating the duplicate token status is not allowed for the associated token type.
- [object DuplicateValueError](duplicatevalueerror.md)
  An error indicating the field’s value is already submitted and a duplicate value is not expected.
- [object ErroneousLineItemReferencedByValidLineItemError](erroneouslineitemreferencedbyvalidlineitemerror.md)
  An error indicating the line item has status erroneously submitted but is referenced by a non-erroneously submitted line item.
- [object ErroneouslySubmittedNotRestatementError](erroneouslysubmittednotrestatementerror.md)
  An error indicating the erroneously submitted line item was not marked as restatement.
- [object ExchangeRateMismatchError](exchangeratemismatcherror.md)
  An error indicating the refund’s referenced buy line item has a different exchange rate.
- [object FieldNotAllowedError](fieldnotallowederror.md)
  An error indicating the provided field is not allowed.
- [object FutureDateError](futuredateerror.md)
  An error indicating the provided date field is in the future and future values are not allowed.
- [object IncorrectAmountTaxInclusiveError](incorrectamounttaxinclusiveerror.md)
  An error indicating the tax exclusive amount plus the tax amount does not equal the tax inclusive amount.
- [object IncorrectNetAmountError](incorrectnetamounterror.md)
  An error indicating the net amount value does not match the expected value.
- [object InvalidTaxInclusiveAmountForSubscriptionPaymentError](invalidtaxinclusiveamountforsubscriptionpaymenterror.md)
  An error indicating the tax inclusive amount must be positive for line items with a subscription payment subscription event.
- [object LineItemCreationDateOutOfRangeError](lineitemcreationdateoutofrangeerror.md)
  An error indicating the line item’s creation date is outside the active range of the token.
- [object LineItemStatusRegressionError](lineitemstatusregressionerror.md)
  An error indicating the status can’t be marked as no line item or unrecognized token after it was previously reported as a line item.
- [object LineItemsNotAllowedForStatusError](lineitemsnotallowedforstatuserror.md)
  An error indicating a line item was provided for an external purchase ID that has the status no line item or unrecognized token.
- [object MaximumLengthExceededError](maximumlengthexceedederror.md)
  An error indicating the field’s maximum length is exceeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/positivevaluerequirederror)*