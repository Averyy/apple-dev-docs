# BooleanResolutionResult

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A Boolean value that matches an intent parameter, or information about why your service can’t determine the value.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object BooleanResolutionResult
```

#### Discussion

Only provide one of the optional properties. If a client receives a result with more than one outcome, such as `needsValue` and `success`, it arbitrarily chooses one and ignores the rest.

## Topics

### Providing a Result
- [object BooleanResolutionResult.ConfirmationRequired](booleanresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the Boolean value before proceeding.
- [object BooleanResolutionResult.Success](booleanresolutionresult/success-data.dictionary.md)
  A Boolean value that successfully matches the intent.

## Relationships

### Inherits From
- [IntentResolutionResult](intentresolutionresult.md)

## See Also

- [object Intent](intent.md)
  A user request for your service to fulfill.
- [object IntentResponse](intentresponse.md)
  Your service’s response to an intent.
- [object UserActivity](useractivity.md)
  The context for playing a media queue.
- [object IntentResolutionResult](intentresolutionresult.md)
  An object that matches a parameter of an intent, or information about why your service can’t determine a value for the parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/booleanresolutionresult)*