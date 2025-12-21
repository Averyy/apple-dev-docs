# readEvents(withEndpointID:clusterID:eventID:params:queue:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func readEvents(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, eventID: NSNumber?, params: MTRReadParams?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/readevents(withendpointid:clusterid:eventid:params:queue:completion:))*