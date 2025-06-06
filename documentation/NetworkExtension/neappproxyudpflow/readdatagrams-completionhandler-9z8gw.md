# readDatagrams(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Read datagrams from the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func readDatagrams(completionHandler: @escaping ([Data]?, [NWEndpoint]?, (any Error)?) -> Void)
```

## Parameters

- `completionHandler`: A block that will be executed by the system on an internal system thread when datagrams have been read from the flow. The block takes the datagrams that were read, the destination endpoints of the datagrams, and an  . If an error occurred while reading then   will be non-nil. See   in   for a list of possible error codes. If the   and   arrays are non-nil but are empty, then no more datagrams can be subsequently read from the flow.

## See Also

- [func writeDatagrams([Data], sentBy: [NWEndpoint], completionHandler: ((any Error)?) -> Void)](neappproxyudpflow/writedatagrams(_:sentby:completionhandler:).md)
  Write datagrams to the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/readdatagrams(completionhandler:)-9z8gw)*