# com.apple.developer.contacts.notes

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app may access the notes in contact entries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 13.0+
- visionOS 1.0+

## Details

- **Name**: `com.apple.developer.contacts.notes`
- **Type**: boolean

## Discussion

When your app loads one or more entries from the user’s contacts — for example, by calling the [`unifiedContacts(matching:keysToFetch:)`](../../Contacts/cncontactstore/unifiedcontacts%28matching,keystofetch%29.md) method — you provide a list of keys specifying the fields to fetch. To request the [`note`](../../Contacts/cncontact/note.md) field using [`CNContactNoteKey`](../../Contacts/cncontactnotekey.md) in iOS 13 or later or macOS 13 or later, your app must have the [`com.apple.developer.contacts.notes`](./com.apple.developer.contacts.notes.md) entitlement. When your app tries to fetch notes without the entitlement, it receives an [`unauthorizedKeys`](../../Contacts/cnerror/unauthorizedkeys.md) error. Your app only needs the entitlement if it reads or writes notes.

Add the entitlement to your app in the Xcode property list editor. Set the entitlement’s type to Boolean, and the corresponding value to `YES`.

![A screenshot of Xcode showing the contact notes entitlement in an app’s entitlements file.](https://developer.apple.com/tutorials/images/com.apple.bundleresources/media-3368935@2x.png)

Before you submit an app with this entitlement to the App Store, you need to get permission to use the entitlement. Request permission at [https://developer.apple.com/contact/request/contact-note-field](https://developer.apple.com/contact/request/contact-note-field).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.contacts.notes)*