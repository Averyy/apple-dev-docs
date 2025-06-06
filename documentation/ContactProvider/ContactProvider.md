# ContactProvider

**Framework**: ContactProvider  
**Kind**: module

Provide contacts managed by your app to the system-wide Contacts ecosystem.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

#### Overview

Use the Contact Provider framework if your app manages its own contacts to make them available in other apps that use the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework. This enables apps like Phone and Mail to provide personal names and images for incoming calls or messages when your app knows the caller or sender. Instead of adding contacts directly with the Contacts framework, your app provides read-only contact items that it can update, and which the person using your app can easily enable, disable, add, or remove. This enables people to organize the contacts they use in your app separately from their personal contacts.

To provide contacts from your app, add an app extension that extends [`ContactProviderExtension`](contactproviderextension.md). The extension is responsible for enumerating contacts that your app manages. Your app manages the extension with the [`ContactProviderManager`](contactprovidermanager.md) class. Use the manager to enable or disable the extension domain, typically using the default domain. After enabling the extension domain, the extension can run and sync contacts, making contacts available to other apps that use the [`Contacts`](https://developer.apple.com/documentation/Contacts) framework.

> 💡 **Tip**: Xcode provides a Contact Provider extension template for use in an existing project to add Contact Provider support. Select your project in the Project navigator, choose Editor > Add Target, or click the Add button (+) in the Projects and Targets list, and choose Contact Provider Extension from the iOS templates.

Xcode provides a Contact Provider extension template for use in an existing project to add Contact Provider support. Select your project in the Project navigator, choose Editor > Add Target, or click the Add button (+) in the Projects and Targets list, and choose Contact Provider Extension from the iOS templates.

There are several ways the extension can run and update contacts. Your app can call the manager’s [`signalEnumerator(for:)`](contactprovidermanager/signalenumerator(for:).md), which loads the extension and asks it to provide an updated set of contacts. An example of using this call is when the app knows that new contacts are available from its server; it can then fetch these contacts and have the extension provide them to the system Contacts database. In addition, when connected to power overnight, Contacts schedules time for all enabled contact provider extension domains to sync at low priority.

A person using the device can see providers in the Settings app and selectively enable or disable them. Disabling a contact provider makes its contacts unavailable to other apps. Deleting the app deletes the extension and all of its contacts.

## Topics

### Creating a contact provider extension
- [protocol ContactProviderExtension](contactproviderextension.md)
  The protocol your app extension implements, which provides contact items to the system-wide Contacts ecosystem.
### Managing an extension in an app
- [class ContactProviderManager](contactprovidermanager.md)
  An interface for the app to control its extension.
### Working with domains
- [protocol ContactProviderDomain](contactproviderdomain.md)
  A domain, including traits like an identifier and display name, used to configure the extension.
- [struct DefaultContactProviderDomain](defaultcontactproviderdomain.md)
  The default domain the extension uses.
### Providing contacts
- [enum ContactItem](contactitem.md)
  An item in the contact database.
- [protocol ContactItemEnumerating](contactitemenumerating.md)
  A protocol to provide enumerators for collections of contact items.
- [protocol ContactItemEnumerator](contactitemenumerator.md)
  A protocol to provide enumerations of all contact items and changed contact items.
### Receiving contacts
- [protocol ContactItemContentObserver](contactitemcontentobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of all items.
- [protocol ContactItemChangeObserver](contactitemchangeobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of changed contact items.
### Supporting types
- [enum ContactProviderError](contactprovidererror.md)
  Errors thrown by the Contact Provider framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ContactProvider)*