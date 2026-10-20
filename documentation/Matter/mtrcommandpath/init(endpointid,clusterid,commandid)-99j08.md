# init(endpointId:clusterId:commandId:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use commandPathWithEndpointID:clusterID:commandID:

## Declaration

```swift
convenience init(endpointId: NSNumber, clusterId: NSNumber, commandId: NSNumber)
```

```objc
+ (instancetype) commandPathWithEndpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId commandId:(NSNumber *) commandId;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommandpath/init(endpointid:clusterid:commandid:)-99j08)*