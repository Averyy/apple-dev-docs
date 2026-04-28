# ManagedApplicationAttributesResponse.ApplicationAttributesItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains a managed app attributes item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManagedApplicationAttributesResponse.ApplicationAttributesItem
```

## Topics

### Objects
- [object ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes](managedapplicationattributesresponse/applicationattributesitem/attributes-data.dictionary.md)
  A dictionary that contains a managed app’s attributes.

## Properties

- `Attributes` (ManagedApplicationAttributesResponse.ApplicationAttributesItem.Attributes): The app’s attributes.
- `Identifier` (string) *(required)*: The app’s bundle identifier. > **Note**:  For a watchOS app, the identifier is the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone to which the watch is paired.

## See Also

- [object ManagedApplicationAttributesResponse.ErrorChainItem](managedapplicationattributesresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationattributesresponse/applicationattributesitem)*