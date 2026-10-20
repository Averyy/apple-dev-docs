# device(_:receivedAttributeReport:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func device(_ nodeID: NSNumber, receivedAttributeReport attributeReport: [[String : Any]])
```

```objc
- (void) device:(NSNumber *) nodeID receivedAttributeReport:(NSArray<NSDictionary<NSString *,id> *> *) attributeReport;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcclientprotocol_mtrdevice/device(_:receivedattributereport:))*