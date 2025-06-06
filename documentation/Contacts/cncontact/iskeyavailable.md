# isKeyAvailable(_:)

**Framework**: Contacts  
**Kind**: method

Determines whether the contact property value for the specified key is fetched.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isKeyAvailable(_ key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value is fetched, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The [`isKeyAvailable(_:)`](cncontact/iskeyavailable(_:).md) or [`areKeysAvailable(_:)`](cncontact/arekeysavailable(_:).md) methods are used when you are not certain of the keys that were fetched. If this method returns [`false`](https://developer.apple.com/documentation/swift/false), refetch the contact using the contact identifier and the keys you want to fetch. Accessing a property that was not fetched will throw [`CNContactPropertyNotFetchedExceptionName`](cncontactpropertynotfetchedexceptionname.md).

## Parameters

- `key`: A contact property key. For a list of valid keys, see  .

## See Also

- [func areKeysAvailable([any CNKeyDescriptor]) -> Bool](cncontact/arekeysavailable(_:).md)
  Determines whether all contact property values for the specified keys are fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/iskeyavailable(_:))*