# highlightProperty(withKey:identifier:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

Highlights the property of the contact being displayed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func highlightProperty(withKey key: String, identifier: String?)
```

```objc
- (void) highlightPropertyWithKey:(NSString *) key identifier:(NSString *) identifier;
```

#### Discussion

When a single value property key is specified, identifier will be ignored.

## Parameters

- `key`: Key of the property to highlight.
- `identifier`: `property` is a multivalue property, the value to highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/highlightproperty(withkey:identifier:))*