# update(_:using:for:)

**Framework**: Network Extension  
**Kind**: method

Updates the verdict for a flow outside the context of any filter data provider callback.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
func update(_ flow: NEFilterSocketFlow, using verdict: NEFilterDataVerdict, for direction: NETrafficDirection)
```

## Parameters

- `flow`: The NEFilterSocketFlow to update the verdict for.
- `verdict`: An   instance.   This must be an   or    verdict, or a data verdict created with the   Swift initializer or  ObjectiveC type method,   .
- `direction`: The direction to which the verdict applies.   Pass   to update the verdict for both the inbound and outbound directions.   This parameter has no effect if the verdict is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/update(_:using:for:))*