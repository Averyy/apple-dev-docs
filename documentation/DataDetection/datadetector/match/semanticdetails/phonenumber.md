# DataDetector.Match.SemanticDetails.PhoneNumber

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents a phone number.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PhoneNumber
```

## Discussion

The [`phoneNumber`](./phonenumber/phonenumber.md) property contains the phone number the data detector found. It may contain an extension, such as a passcode or an office extension. The [`label`](./phonenumber/label.md) property may contain a value suitable to populate a label when creating a contact.

## Topics

### Components of a phone number
- [let phoneNumber: String](./phonenumber/phonenumber.md)
  A string that contains the phone number the data detector found.
- [let label: String?](./phonenumber/label.md)
  An optional string that may contain a value suitable to populate a label when creating a contact.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/phonenumber)*