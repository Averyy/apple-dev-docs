# Common data types

**Framework**: App Intents

Use framework-defined types for common parameter and result data types such as contacts, files, currencies, and more.

#### Overview

When creating your app intents or app entities, use existing types for parameters and properties whenever possible. The App Intents framework provides common data types to represent people, files, currencies, and more. Choose the type that matches your app’s data and fill its properties with data from your app.

## Topics

### Contacts
- [struct IntentPerson](intentperson.md)
  Information that identifies a person participating in an intents-based interaction.
### Files
- [struct IntentFile](intentfile.md)
  An interface for providing an app entity that represents an on-disk file or file-based resource.
### Media
- [struct AudioSearch](../MediaIntents/AudioSearch.md)
  Results and metadata for a person’s audio search and playback request with Siri.
- [Media Intents](../MediaIntents/MediaIntents.md)
  Enable people to use Siri to find and play media from your app.
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
- [struct IntentResponseStream](intentresponsestream.md)

## See Also

- [App intents](app-intents.md)
  Make your app’s custom actions available to the system by using app intent types.
- [App entities](app-entities.md)
  Make your app’s core types and data concepts available to the system using app entity types.
- [App enums](app-enums.md)
  Make your app’s enumerations and predefined values available to the system by using app enum types.
- [App extension](app-extension.md)
  Deliver app intents in an app extension or other package that lives outside your app’s code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/common-data-types)*