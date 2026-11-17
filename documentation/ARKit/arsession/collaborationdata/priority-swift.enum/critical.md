# ARSession.CollaborationData.Priority.critical

**Framework**: ARKit  
**Kind**: case  
**Role**: Case

A priority that indicates that collaboration depends on this data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
case critical
```

```c
ARCollaborationDataPriorityCritical
```

## Discussion

ARKit sets the data priority to critical when the data is important for establishing or continuing a collaborative session. For best results, use network transmission mechanisms that ensure delivery, such as MCSessionSendDataModeReliable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/collaborationdata/priority-swift.enum/critical)*