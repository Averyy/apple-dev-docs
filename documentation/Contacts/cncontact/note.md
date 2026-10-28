# note

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

A string containing notes for the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var note: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * note;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * note;
```

## Mentions

- [Accessing the contact store](../accessing-the-contact-store.md)

## Discussion

To fetch the `note` property in iOS 13 or later or macOS 13 or later, add the [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md) entitlement to your app. The entitlement requires permission from Apple to use, and you can’t publicly distribute your app until you have permission to use it. For more information about adding the entitlement and getting permission, see [`com.apple.developer.contacts.notes`](../../BundleResources/entitlements/com.apple.developer.contacts.notes.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/note)*