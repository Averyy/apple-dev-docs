# inputText(_:key:modifiers:client:)

**Framework**: Objective-C Runtime  
**Kind**: method

Receives Unicode, the key code that generated it, and any modifier flags.

**Availability**:
- macOS ?+

## Declaration

```swift
func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the input is  accepted; otherwise [`NO`](no.md).

## Parameters

- `string`: The text input by the client.
- `keyCode`: The key code for the associated Unicode.
- `flags`: The modifier flags.
- `sender`: The client object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:key:modifiers:client:))*