# inputText(_:client:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Handles key down events that do not map to an action method.

**Availability**:
- macOS

## Declaration

```swift
func inputText(_ string: String!, client sender: Any!) -> Bool
```

```objc
- (BOOL) inputText:(NSString *) string client:(id) sender;
```

#### Return Value

[`YES`](../yes.md) if the input is accepted; otherwise [`NO`](../no.md).

#### Discussion

An input method should implement this method when using key binding (that is, it implements [`didCommand(by:client:)`](./didcommand%28by,client%29.md)).

## Parameters

- `string`: The key down event, which is the text input by the client.
- `sender`: The client object sending the key down events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:client:))*