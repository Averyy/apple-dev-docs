# areKeysAvailable(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) areKeysAvailable:(NSArray<id<CNKeyDescriptor>> *) keyDescriptors;
```

#### Return Value

[`true`](../../Swift/true.md) if all the values are fetched; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The [`isKeyAvailable(_:)`](./iskeyavailable%28_%29.md) or [`areKeysAvailable(_:)`](./arekeysavailable%28_%29.md) methods are used where you are not certain of the keys that when fetched. If this method returns [`false`](../../Swift/false.md), refetch the contact using the contact identifier and the keys you want to fetch. Accessing a property that was not fetched will throw an [`CNContactPropertyNotFetchedExceptionName`](../cncontactpropertynotfetchedexceptionname.md) exception.

## Parameters

- `keyDescriptors`: An array of contact property keys and/or key descriptors from contact objects.

## See Also

### Checking the Availability of Data
- [func isKeyAvailable(String) -> Bool](./iskeyavailable%28_%29.md)
  Determines whether the contact property value for the specified key is fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/arekeysavailable(_:))*