# vCardRepresentation()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the vCard representation of the person record as a data object in vCard format.

**Availability**:
- macOS

## Declaration

```swift
func vCardRepresentation() -> Data!
```

```objc
- (NSData *) vCardRepresentation;
```

## Return Value

A data object containing the vCard representation of the person record.

## See Also

### Importing and Exporting vCard Formatted Files
- [init!(VCardRepresentation: Data!)](./init%28vcardrepresentation%29-5c7h8.md)
  Returns an `ABPerson` instance initialized with the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abperson/vcardrepresentation())*