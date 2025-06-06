# Common types

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/common-data-types)*