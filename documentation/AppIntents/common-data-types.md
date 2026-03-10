# Common data types

**Framework**: App Intents

Specify common types that your app supports, including currencies, files, and contacts.

#### Overview

Use these types to manage specific types of data when you create a parameter for an app intent or a property for an app entity.

## Topics

### Contacts
- [struct IntentPerson](intentperson.md)
  Information that identifies a person participating in an intents-based interaction.
### Files
- [struct IntentFile](intentfile.md)
  An interface for providing an app entity that represents an on-disk file or file-based resource.
### Monetary types
- [struct IntentCurrencyAmount](intentcurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [struct IntentPaymentMethod](intentpaymentmethod.md)
  Information about a form of payment supported by your app.
### Items and collections
- [struct IntentItem](intentitem.md)
  A type describing a value returned from a dynamic options provider, plus information about how to display it to users.
- [struct IntentItemCollection](intentitemcollection.md)
  Return this object to provide an advanced list of options, optionally divided in sections.
- [struct IntentItemSection](intentitemsection.md)
  An object you use to divide dynamic options into sections.
- [struct IntentCollectionSize](intentcollectionsize.md)

## See Also

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Static parameter types](app-enums.md)
  Types that represent an enumerable list of static parameter values.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/common-data-types)*