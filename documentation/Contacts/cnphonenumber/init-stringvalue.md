# init(stringValue:)

**Framework**: Contacts  
**Kind**: init

Returns a new phone number object initialized with the specified phone number string.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(stringValue string: String)
```

#### Return Value

A newly initialized phone number object.

#### Discussion

You should initialize this with a phone number string. This method returns `nil` when the value of `string` is `nil`.

## Parameters

- `string`: A string value with which to initializes the phone number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnphonenumber/init(stringvalue:))*