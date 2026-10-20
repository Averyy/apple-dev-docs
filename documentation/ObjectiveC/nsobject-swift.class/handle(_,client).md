# handle(_:client:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Handles key down and mouse events.

**Availability**:
- macOS

## Declaration

```swift
func handle(_ event: NSEvent!, client sender: Any!) -> Bool
```

```objc
- (BOOL) handleEvent:(NSEvent *) event client:(id) sender;
```

#### Return Value

[`YES`](../yes.md) if the event is handled; otherwise [`NO`](../no.md).

## Parameters

- `event`: The event to handle.
- `sender`: The client object sending the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handle(_:client:))*