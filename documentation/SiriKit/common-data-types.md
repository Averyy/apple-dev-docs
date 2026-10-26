# Common Data Types

**Framework**: SiriKit  
**Role**: API Collection

Manage common data types such as strings, dates, currencies, images, and contacts.

## Topics

### Contacts
- [class INPerson](../Intents/inperson.md)
  Information about a person participating in a SiriKit interaction.
- [class INPersonHandle](../Intents/inpersonhandle.md)
  The identifying information for a user of your app.
- [struct INPersonHandleLabel](../Intents/inpersonhandlelabel.md)
  Constants describing how the person handle relates to the user.
### Images
- [class INImage](../Intents/inimage.md)
  Image data inside an Intents extension or Intents UI extension.
### String
- [class INSpeakableString](../Intents/inspeakablestring.md)
  A custom phrase to be resolved by an Intents extension.
- [protocol INSpeakable](../Intents/inspeakable.md)
  Pronunciation hints for strings used in a spoken interface.
### Monetary
- [class INCurrencyAmount](../Intents/incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPriceRange](../Intents/inpricerange.md)
  Price information, as a range of possible values.
### Date
- [class INDateComponentsRange](../Intents/indatecomponentsrange.md)
  A span of time.
- [class INRecurrenceRule](../Intents/inrecurrencerule.md)
  An object that describes the pattern to use when repeating an event.
### Logical
- [enum INConditionalOperator](../Intents/inconditionaloperator.md)
  Constants indicating how search attributes are interpreted.
### Files
- [class INFile](../Intents/infile.md)
  An object that describes a file.
### Custom Objects
- [class INObject](../Intents/inobject.md)
  A representation of a custom intent parameter or response property.
- [class INObjectCollection](../Intents/inobjectcollection.md)
- [class INObjectSection](../Intents/inobjectsection.md)

## See Also

### Intents
- [Dispatching intents to handlers](./dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Resolving and Handling Intents](./resolving-and-handling-intents.md)
  Resolve, confirm, and handle user requests for your app’s services.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/common-data-types)*