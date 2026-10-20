# ENTemporaryExposureKey

**Framework**: Exposure Notification  
**Kind**: class  
**Role**: Class

The key used to generate rolling proximity identifiers.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
class ENTemporaryExposureKey
```

```objc
@interface ENTemporaryExposureKey : NSObject
```

#### Overview

> ❗ **Important**:  This class is available in iOS 12.5, and in iOS 13.5 and later.

Upon a positive diagnosis, the user is allowed to submit their temporary exposure keys to their Health Authority server as diagnosis keys. Use [`getDiagnosisKeys(completionHandler:)`](./enmanager/getdiagnosiskeys%28completionhandler%29.md) to obtain the user’s diagnosis keys for submission.

## Topics

### Exposure Criteria
- [var transmissionRiskLevel: ENRiskLevel](./entemporaryexposurekey/transmissionrisklevel.md)
  The risk of transmission associated with the person a key came from.
- [var rollingPeriod: ENIntervalNumber](./entemporaryexposurekey/rollingperiod.md)
  The length of time that this key is valid.
- [var keyData: Data](./entemporaryexposurekey/keydata.md)
  The temporary exposure key information.
- [var rollingStartNumber: ENIntervalNumber](./entemporaryexposurekey/rollingstartnumber.md)
  A number that indicates when a key’s rolling period started.
- [typealias ENIntervalNumber](./enintervalnumber.md)
  A number assigned to each 10-minute window shared between all devices participating in the protocol.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Obtaining Exposure Keys
- [func getDiagnosisKeys(completionHandler: ([ENTemporaryExposureKey]?, (any Error)?) -> Void)](./enmanager/getdiagnosiskeys%28completionhandler%29.md)
  Requests the temporary exposure keys from the user’s device to share with a server.
- [func getTestDiagnosisKeys(completionHandler: ([ENTemporaryExposureKey]?, (any Error)?) -> Void)](./enmanager/gettestdiagnosiskeys%28completionhandler%29.md)
  Requests the temporary exposure keys, including the current key, used by this device for testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/entemporaryexposurekey)*