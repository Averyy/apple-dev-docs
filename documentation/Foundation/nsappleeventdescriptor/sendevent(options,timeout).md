# sendEvent(options:timeout:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends an Apple event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func sendEvent(options sendOptions: NSAppleEventDescriptor.SendOptions = [], timeout timeoutInSeconds: TimeInterval) throws -> NSAppleEventDescriptor
```

```objc
- (NSAppleEventDescriptor *) sendEventWithOptions:(NSAppleEventSendOptions) sendOptions timeout:(NSTimeInterval) timeoutInSeconds error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendevent(options:timeout:))*