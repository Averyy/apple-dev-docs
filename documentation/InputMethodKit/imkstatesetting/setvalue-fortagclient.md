# setValue(_:forTag:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Set the value for the provided key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setValue(_ value: Any!, forTag tag: Int, client sender: Any!)
```

## Parameters

- `value`: The value, specified as the appropriate object (such as  ), to set.
- `tag`: The key whose value you want to set.
- `sender`: The client setting the value.

## See Also

- [func value(forTag: Int, client: Any!) -> Any!](imkstatesetting/value(fortag:client:).md)
  Returns a value object whose key is the provided tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/setvalue(_:fortag:client:))*