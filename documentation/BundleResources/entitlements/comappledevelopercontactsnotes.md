# com.apple.developer.contacts.notes

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may access the notes in contact entries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 13.0+
- visionOS 1.0+

#### Discussion

When your app loads one or more entries from the user’s contacts — for example, by calling the [`unifiedContacts(matching:keysToFetch:)`](https://developer.apple.com/documentation/Contacts/CNContactStore/unifiedContacts(matching:keysToFetch:)) method — you provide a list of keys specifying the fields to fetch. To request the [`note`](https://developer.apple.com/documentation/Contacts/CNContact/note) field using [`CNContactNoteKey`](https://developer.apple.com/documentation/Contacts/CNContactNoteKey) in iOS 13 or later or macOS 13 or later, your app must have the [`com.apple.developer.contacts.notes`](entitlements/com.apple.developer.contacts.notes.md) entitlement. When your app tries to fetch notes without the entitlement, it receives an [`unauthorizedKeys`](https://developer.apple.com/documentation/Contacts/CNError/unauthorizedKeys) error. Your app only needs the entitlement if it reads or writes notes.

Add the entitlement to your app in the Xcode property list editor. Set the entitlement’s type to Boolean, and the corresponding value to `YES`.

![A screenshot of Xcode showing the contact notes entitlement in an app’s entitlements file.](https://docs-assets.developer.apple.com/published/6173e6814a1382b81ba3725b2a5225cc/media-3368935%402x.png)

Before you submit an app with this entitlement to the App Store, you need to get permission to use the entitlement. Request permission at [`https://developer.apple.com/contact/request/contact-note-field`](https://developer.apple.comhttps://developer.apple.com/contact/request/contact-note-field).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.contacts.notes)*