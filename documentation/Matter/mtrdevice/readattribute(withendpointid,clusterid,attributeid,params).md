# readAttribute(withEndpointID:clusterID:attributeID:params:)

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
func readAttribute(withEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?) -> [String : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) readAttributeWithEndpointID:(NSNumber *) endpointID clusterID:(NSNumber *) clusterID attributeID:(NSNumber *) attributeID params:(MTRReadParams *) params;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/readattribute(withendpointid:clusterid:attributeid:params:))*