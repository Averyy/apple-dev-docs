# encode(to:)

**Framework**: FamilyControls  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus/encode(to:))*