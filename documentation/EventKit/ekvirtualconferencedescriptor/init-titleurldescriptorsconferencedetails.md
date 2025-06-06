# init(title:urlDescriptors:conferenceDetails:)

**Framework**: EventKit  
**Kind**: init

Creates an object that describes a virtual conference, including a name and URL to join the conference.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(title: String?, urlDescriptors URLDescriptors: [EKVirtualConferenceURLDescriptor], conferenceDetails: String?)
```

#### Return Value

An object that describes a virtual conference.

## Parameters

- `title`: The user-visible name of the virtual conference.
- `URLDescriptors`: An array that contains objects with details about where to join the virtual conference. Calendar uses the first URL descriptor as the preferred way for users to join a virtual conference, and displays additional URLs as links in the virtual conference details.
- `conferenceDetails`: Additional information about the conference that users may find helpful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekvirtualconferencedescriptor/init(title:urldescriptors:conferencedetails:))*