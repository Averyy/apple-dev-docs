# Error messages and codes

**Framework**: External Purchase Server API

Error messages and codes for reports and endpoints.

## Topics

### Error objects for reports
- [object DateTooFarInPastError](datetoofarinpasterror.md)
  An error indicating that a provided date is too far in the past.
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
- [object LineItemStatusRegressionError](lineitemstatusregressionerror.md)
  An error indicating the status can’t be marked as no line item or unrecognized token after it was previously reported as a line item.
- [object LineItemsNotAllowedForStatusError](lineitemsnotallowedforstatuserror.md)
  An error indicating a line item was provided for an external purchase ID that has the status no line item or unrecognized token.
- [object MaximumLengthExceededError](maximumlengthexceedederror.md)
  An error indicating the field’s maximum length is exceeded.
- [object MissingLineItemsForStatusError](missinglineitemsforstatuserror.md)
  An error indicating the external purchase ID has the status line item but is missing line items.
- [object NegativeValueNotAllowedError](negativevaluenotallowederror.md)
  An error indicating the field does not allow a negative value.
- [object NetAmountMismatchError](netamountmismatcherror.md)
  An error indicating two line items involved in the same net amount calculation have different net amount values.
- [object NonInitialBuyReferencedByBuyError](noninitialbuyreferencedbybuyerror.md)
  An error indicating the line item does not have subscription event initial buy but is referenced by a subscription line item with event type buy.
- [object NotFoundError](notfounderror.md)
  An error indicating the referenced value was not found.
- [object OmittedFieldError](omittedfielderror.md)
  An error indicating a required field is missing.
- [object PositiveValueRequiredError](positivevaluerequirederror.md)
  An error indicating the field requires a positive value.
- [object PricingCurrencyMismatchError](pricingcurrencymismatcherror.md)
  An error indicating the refund’s referenced buy line item has a different pricing currency.
- [object ReferenceInvalidSubscriptionEventError](referenceinvalidsubscriptioneventerror.md)
  An error indicating the referenced line item has no subscription event or its subscription event is not subscription start.
- [object ReferenceLineItemNotABuyError](referencelineitemnotabuyerror.md)
  An error indicating the referenced line item is not a buy.
- [object ReferencedCreationDateIncompatibleError](referencedcreationdateincompatibleerror.md)
  An error indicating the referenced line item has a creation date after the line item’s creation date.
- [object RefundNotAllowedCreationDateError](refundnotallowedcreationdateerror.md)
  An error indicating the refund isn’t allowed for the line item because its creation date is too far in the past.
- [object RefundReferencedByRefundError](refundreferencedbyrefunderror.md)
  An error indicating the line item has the refund event type but is referenced by a different line item that also has that type.
- [object RestatementCreationDateMismatchError](restatementcreationdatemismatcherror.md)
  An error indicating the creation date of the restatement line item doesn’t match the creation date of the original line item.
- [object RestatementNotAllowedCreationDateError](restatementnotallowedcreationdateerror.md)
  An error indicating that restatement failed because the creation date is too far in the past.
- [object RepeatErroneousSubmissionError](repeaterroneoussubmissionerror.md)
  An error indicating the line item has status erroneously submitted but its previous version was already marked erroneously submitted.
- [object ReportingCurrencyExchangeNotAllowedError](reportingcurrencyexchangenotallowederror.md)
  An error indicating that the reporting currency, which reports a currency exchange, isn’t allowed.
- [object ReportingCurrencyMismatchError](reportingcurrencymismatcherror.md)
  An error indicating the refund’s referenced buy line item has a different reporting currency.
- [object SelfReferenceError](selfreferenceerror.md)
  An error indicating the line item references itself.
- [object SimultaneousSubmissionError](simultaneoussubmissionerror.md)
  An error indicating one or more simultaneous submissions of reports reference the same data.
- [object StartDateAfterEndDateError](startdateafterenddateerror.md)
  An error indicating the subscription data submitted is invalid because the start date is after the end date.
- [object SubscriptionStartNonZeroDaysPaidServiceError](subscriptionstartnonzerodayspaidserviceerror.md)
  An error indicating that the subscription days of paid service value is invalid because it’s non-zero for a subscription start line item.
- [object TaxCountryMismatchError](taxcountrymismatcherror.md)
  An error indicating the refund’s referenced buy line item has a different tax country.
- [object UnknownEnumError](unknownenumerror.md)
  An error indicating the submission contained an invalid enum value.
- [object ValidLineItemReferencesErroneousLineItemError](validlineitemreferenceserroneouslineitemerror.md)
  An error indicating the line item references an erroneously submitted line item, but the line item itself isn’t erroneously submitted.
### Error types
- [type errorCode](errorcode.md)
  An integer value that represents an error in the External Purchase Server API.
- [type errorMessage](errormessage.md)
  A string that describes an error.
- [type fieldName](fieldname.md)
  A string that names a field of a line item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/errorcodes)*