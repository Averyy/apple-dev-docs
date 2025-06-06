# init(version:refcon:getDecodeTimeStamp:getPresentationTimeStamp:getDuration:isDataReady:compare:dataBecameReadyNotification:getSize:)

**Framework**: Core Media  
**Kind**: init

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(version: UInt32, refcon: UnsafeMutableRawPointer?, getDecodeTimeStamp: CMBufferGetTimeCallback?, getPresentationTimeStamp: CMBufferGetTimeCallback?, getDuration: CMBufferGetTimeCallback, isDataReady: CMBufferGetBooleanCallback?, compare: CMBufferCompareCallback?, dataBecameReadyNotification: Unmanaged<CFString>?, getSize: CMBufferGetSizeCallback?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/init(version:refcon:getdecodetimestamp:getpresentationtimestamp:getduration:isdataready:compare:databecamereadynotification:getsize:))*