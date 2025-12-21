# ARKitSession.Event.dataProviderStateChanged(dataProviders:newState:error:)

**Framework**: ARKit  
**Kind**: case

An event that represents a state change of one or more of the data providers associated with a session.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case dataProviderStateChanged(dataProviders: [any DataProvider], newState: DataProviderState, error: ARKitSession.Error?)
```

## Parameters

- `dataProviders`: The data providers whose state has changed.
- `newState`: The new data provider state, which triggered the event.
- `error`: An   associated with the state change, if any. This is only applicable to   updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/event/dataproviderstatechanged(dataproviders:newstate:error:))*