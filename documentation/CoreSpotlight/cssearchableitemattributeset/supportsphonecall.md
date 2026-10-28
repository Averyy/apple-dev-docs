# supportsPhoneCall

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var supportsPhoneCall: NSNumber? { get set }
```

```objc
@property (strong, nullable) NSNumber * supportsPhoneCall;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

## Discussion

When an item includes the [`phoneNumbers`](./phonenumbers.md) property, the phone number can be used to initiate phone calls. You can use the [`supportsPhoneCall`](./supportsphonecall.md) property to indicate when making a phone call is appropriate and likely to be a primary action for the user. For example, you might set [`supportsPhoneCall`](./supportsphonecall.md) to `1` for an item that represents a business, but not for an item that represents an academic paper that lists the phone numbers of the authors or the institution.

## See Also

### Describing supporting actions
- [var actionIdentifiers: [String]](./actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsNavigation: NSNumber?](./supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var sharedItemContentType: UTType?](./shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.
- [let CSActionIdentifier: String](../csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/supportsphonecall)*