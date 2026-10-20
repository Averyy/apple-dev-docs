# isKeyAvailable(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isKeyAvailable:(NSString *) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the value is fetched, otherwise [`false`](../../Swift/false.md).

#### Discussion

The [`isKeyAvailable(_:)`](./iskeyavailable%28_%29.md) or [`areKeysAvailable(_:)`](./arekeysavailable%28_%29.md) methods are used when you are not certain of the keys that were fetched. If this method returns [`false`](../../Swift/false.md), refetch the contact using the contact identifier and the keys you want to fetch. Accessing a property that was not fetched will throw [`CNContactPropertyNotFetchedExceptionName`](../cncontactpropertynotfetchedexceptionname.md).

## Parameters

- `key`: A contact property key. For a list of valid keys, see [Contact Keys](../contact-keys.md).

## See Also

### Checking the Availability of Data
- [func areKeysAvailable([any CNKeyDescriptor]) -> Bool](./arekeysavailable%28_%29.md)
  Determines whether all contact property values for the specified keys are fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/iskeyavailable(_:))*