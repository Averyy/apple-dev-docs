# writeAttribute(withEndpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func writeAttribute(withEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber, timedWriteTimeout timeout: NSNumber?)
```

```objc
- (void) writeAttributeWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID attributeID:(NSNumber *) attributeID value:(id) value expectedValueInterval:(NSNumber *) expectedValueInterval timedWriteTimeout:(NSNumber *) timeout;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/writeattribute(withendpointid:clusterid:attributeid:value:expectedvalueinterval:timedwritetimeout:))*