# Resolving and Handling Intents

**Framework**: SiriKit  
**Role**: API Collection

Resolve, confirm, and handle user requests for your app’s services.

#### Overview

SiriKit works with your Intents app extension to verify that you are able to fulfill the user’s request based on the provided information. During the resolution phase, you validate the individual parameters of an intent object and ask SiriKit for clarifications as needed. During the confirmation phase, you perform one final check of all intent parameters and verify that your services are ready to fulfill the intent. If you validate the intent successfully, SiriKit asks you to handle the intent.

> ❗ **Important**:  watchOS does not support all intents. For example, an Intents app extension on watchOS cannot start a video call, set message attributes, or handle any intents in the CarPlay domain. Check the availability of any intents before trying to handle them on watchOS.

## Topics

### Resolving and Handling Intents
- [Resolving the Parameters of an Intent](./resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Confirming the Details of an Intent](./confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](./handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
### Responses
- [class INIntentResolutionResult](../Intents/inintentresolutionresult.md)
  A resolution result for a parameter of an intent object.
- [class INIntentResponse](../Intents/inintentresponse.md)
  Your response to an intent object.

## See Also

### Intents
- [Dispatching intents to handlers](./dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [class INIntent](../Intents/inintent.md)
  A request to fulfill in your app or Intents extension.
- [class INIntentResponse](../Intents/inintentresponse.md)
  Your response to an intent object.
- [Intent Handling Infrastructure](./intent-handling-infrastructure.md)
  Specify required permissions and provide handlers for the intents your app supports, and configure app extensions.
- [Providing Hands-Free App Control with Intents](./providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Resolution Results](./resolution-results.md)
  Resolve common types of data like strings and dates into specific values that your app recognizes.
- [Common Data Types](./common-data-types.md)
  Manage common data types such as strings, dates, currencies, images, and contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/resolving-and-handling-intents)*