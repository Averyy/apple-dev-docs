# highlightProperty(withKey:identifier:)

**Framework**: Contacts UI  
**Kind**: method

Highlights the property of the contact being displayed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func highlightProperty(withKey key: String, identifier: String?)
```

#### Discussion

When a single value property key is specified, identifier will be ignored.

## Parameters

- `key`: Key of the property to highlight.
- `identifier`:   is a multivalue property, the value to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/highlightproperty(withkey:identifier:))*