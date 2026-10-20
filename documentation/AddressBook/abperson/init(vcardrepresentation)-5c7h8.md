# init(VCardRepresentation:)

**Framework**: Address Book  
**Kind**: init  
**Role**: Initializer

Returns an `ABPerson` instance initialized with the given data.

**Availability**:
- macOS

## Declaration

```swift
init!(VCardRepresentation vCardData: Data!)
```

#### Return Value

An `ABPerson` instance initialized with the given data.

#### Discussion

Version 2.1 and 3.0 of the vCard format are supported. If `vCardData` is `nil` or is not a valid vCard format, this method returns `nil`.

## Parameters

- `vCardData`: A data object containing a vCard representation of a person record.

## See Also

### Importing and Exporting vCard Formatted Files
- [func vCardRepresentation() -> Data!](./vcardrepresentation%28%29.md)
  Returns the vCard representation of the person record as a data object in vCard format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/init(vcardrepresentation:)-5c7h8)*