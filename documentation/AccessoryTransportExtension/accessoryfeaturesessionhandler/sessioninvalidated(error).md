# sessionInvalidated(error:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the handler when its feature session ends.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func sessionInvalidated(error: (any Error)?)
```

## Discussion

Release your reference to the session when the system calls this method.

## Parameters

- `error`: An optional error that indicates why the session ends. A `nil` value indicates ordinary completion.

## See Also

### Handling the session life cycle
- [func sessionStarted(Self.Session)](./sessionstarted%28_%29.md)
  Notifies the handler when its feature session starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesessionhandler/sessioninvalidated(error:))*