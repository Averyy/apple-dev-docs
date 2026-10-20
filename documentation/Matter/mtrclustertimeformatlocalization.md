# MTRClusterTimeFormatLocalization

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterTimeFormatLocalization
```

```objc
@interface MTRClusterTimeFormatLocalization : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustertimeformatlocalization/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustertimeformatlocalization/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveCalendarType(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributeactivecalendartype%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHourFormat(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributehourformat%28with%29.md)
- [func readAttributeSupportedCalendarTypes(with: MTRReadParams?) -> [String : Any]?](./mtrclustertimeformatlocalization/readattributesupportedcalendartypes%28with%29.md)
- [func writeAttributeActiveCalendarType(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustertimeformatlocalization/writeattributeactivecalendartype%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeActiveCalendarType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustertimeformatlocalization/writeattributeactivecalendartype%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeHourFormat(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustertimeformatlocalization/writeattributehourformat%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeHourFormat(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustertimeformatlocalization/writeattributehourformat%28withvalue,expectedvalueinterval,params%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertimeformatlocalization)*