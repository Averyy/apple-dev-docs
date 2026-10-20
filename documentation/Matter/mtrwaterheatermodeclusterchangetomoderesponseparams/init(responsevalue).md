# init(responseValue:)

**Framework**: Matter  
**Kind**: init

Initialize an MTRWaterHeaterModeClusterChangeToModeResponseParams with a response-value dictionary of the sort that MTRDeviceResponseHandler would receive.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
init(responseValue: [String : Any]) throws
```

#### Discussion

Will return nil and hand out an error if the response-value dictionary is not a command data response or is not the right command response.

Will return nil and hand out an error if the data response does not match the known schema for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrwaterheatermodeclusterchangetomoderesponseparams/init(responsevalue:))*