# value(forTag:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a value object whose key is the provided tag.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func value(forTag tag: Int, client sender: Any!) -> Any!
```

```objc
- (id) valueForTag:(long) tag client:(id) sender;
```

## Return Value

The value object.

## Parameters

- `tag`: The key whose value you want to retrieve.
- `sender`: The client requesting the value.

## See Also

### Getting and Setting Values
- [func setValue(Any!, forTag: Int, client: Any!)](./setvalue%28_,fortag,client%29.md)
  Set the value for the provided key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/value(fortag:client:))*