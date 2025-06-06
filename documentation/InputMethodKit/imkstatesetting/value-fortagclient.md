# value(forTag:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Returns a value object whose key is the provided tag.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func value(forTag tag: Int, client sender: Any!) -> Any!
```

#### Return Value

The value object.

## Parameters

- `tag`: The key whose value you want to retrieve.
- `sender`: The client requesting the value.

## See Also

- [func setValue(Any!, forTag: Int, client: Any!)](imkstatesetting/setvalue(_:fortag:client:).md)
  Set the value for the provided key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/value(fortag:client:))*