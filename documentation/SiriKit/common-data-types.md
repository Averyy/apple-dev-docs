# Common Data Types

**Framework**: SiriKit  
**Role**: API Collection

Manage common data types such as strings, dates, currencies, images, and contacts.

## Topics

### Contacts
- [class INPerson](https://developer.apple.com/documentation/intents/inperson)
  Information about a person participating in a SiriKit interaction.
- [class INPersonHandle](https://developer.apple.com/documentation/intents/inpersonhandle)
  The identifying information for a user of your app.
- [struct INPersonHandleLabel](https://developer.apple.com/documentation/intents/inpersonhandlelabel)
  Constants describing how the person handle relates to the user.
### Images
- [class INImage](https://developer.apple.com/documentation/intents/inimage)
  Image data inside an Intents extension or Intents UI extension.
### String
- [class INSpeakableString](https://developer.apple.com/documentation/intents/inspeakablestring)
  A custom phrase to be resolved by an Intents extension.
- [protocol INSpeakable](https://developer.apple.com/documentation/intents/inspeakable)
  Pronunciation hints for strings used in a spoken interface.
### Monetary
- [class INCurrencyAmount](https://developer.apple.com/documentation/intents/incurrencyamount)
  An amount of money to transfer during a financial transaction.
- [class INPriceRange](https://developer.apple.com/documentation/intents/inpricerange)
  Price information, as a range of possible values.
### Date
- [class INDateComponentsRange](https://developer.apple.com/documentation/intents/indatecomponentsrange)
  A span of time.
- [class INRecurrenceRule](https://developer.apple.com/documentation/intents/inrecurrencerule)
  An object that describes the pattern to use when repeating an event.
### Logical
- [enum INConditionalOperator](https://developer.apple.com/documentation/intents/inconditionaloperator)
  Constants indicating how search attributes are interpreted.
### Files
- [class INFile](https://developer.apple.com/documentation/intents/infile)
  An object that describes a file.
### Custom Objects
- [class INObject](https://developer.apple.com/documentation/intents/inobject)
  A representation of a custom intent parameter or response property.
- [class INObjectCollection](https://developer.apple.com/documentation/intents/inobjectcollection)
- [class INObjectSection](https://developer.apple.com/documentation/intents/inobjectsection)

## See Also

### Intents
- [Dispatching intents to handlers](./dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Resolving and Handling Intents](./resolving-and-handling-intents.md)
  Resolve, confirm, and handle user requests for your app’s services.
- [class INIntent](https://developer.apple.com/documentation/intents/inintent)
  A request to fulfill in your app or Intents extension.
- [class INIntentResponse](https://developer.apple.com/documentation/intents/inintentresponse)
  Your response to an intent object.
- [Intent Handling Infrastructure](./intent-handling-infrastructure.md)
  Specify required permissions and provide handlers for the intents your app supports, and configure app extensions.
- [Providing Hands-Free App Control with Intents](./providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Resolution Results](./resolution-results.md)
  Resolve common types of data like strings and dates into specific values that your app recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/common-data-types)*