# init(id:state:guidanceState:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electrical load event session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
init(id: UUID, state: ElectricHVACLoadEvent.Session.State, guidanceState: ElectricHVACLoadEvent.Session.GuidanceState)
```

## Parameters

- `id`: The unique identifier for the session.
- `state`: The state of the session.
- `guidanceState`: Identifies the provided guidance and its usability by the load device


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/init(id:state:guidancestate:))*