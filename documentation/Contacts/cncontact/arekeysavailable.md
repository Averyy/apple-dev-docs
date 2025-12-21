# areKeysAvailable(_:)

**Framework**: Contacts  
**Kind**: method

Determines whether all contact property values for the specified keys are fetched.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func areKeysAvailable(_ keyDescriptors: [any CNKeyDescriptor]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if all the values are fetched; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The [`isKeyAvailable(_:)`](cncontact/iskeyavailable(_:).md) or [`areKeysAvailable(_:)`](cncontact/arekeysavailable(_:).md) methods are used where you are not certain of the keys that when fetched. If this method returns [`false`](https://developer.apple.com/documentation/Swift/false), refetch the contact using the contact identifier and the keys you want to fetch. Accessing a property that was not fetched will throw an [`CNContactPropertyNotFetchedExceptionName`](cncontactpropertynotfetchedexceptionname.md) exception.

## Parameters

- `keyDescriptors`: An array of contact property keys and/or key descriptors from contact objects.

## See Also

- [func isKeyAvailable(String) -> Bool](cncontact/iskeyavailable(_:).md)
  Determines whether the contact property value for the specified key is fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/arekeysavailable(_:))*