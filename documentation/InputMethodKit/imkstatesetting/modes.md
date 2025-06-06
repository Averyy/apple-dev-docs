# modes(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Returns the modes dictionary associated with the input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func modes(_ sender: Any!) -> [AnyHashable : Any]!
```

#### Return Value

The modes dictionary associated with the input method.

#### Discussion

Typically a client object calls this method to to build the text input menu. By calling the input method rather than reading the modes from the `Info.plist` file, the input method can dynamically modify the modes supported.

## Parameters

- `sender`: The client object requesting the modes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/modes(_:))*