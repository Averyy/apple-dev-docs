# experimentID

**Framework**: File Provider  
**Kind**: property

System interpreted user info key When setting a value to that user info on a domain, the system will ingest this value. If user has given their consent for telemetry, this value will be used to decorate telemetry messages sent by the FileProvider subsystem. The telemetry messages can be then later on retrieved by developers along with the other metrics through the CloudKit console as detailed here: https://developer.apple.com/documentation/fileprovider/exporting-file-provider-metrics-data?language=objc This will help developers triaging data they receive from testing population compared to regular users The value must either be a NSNumber between [0 - 31]. If it’s not in that range, or if it is not a NSNumber, any call to addDomain with that invalid UserInfo dictionary will fail with a EINVAL POSIX NSError. To update this value, the provider must call addDomain with an updated userInfo dictionary

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static let experimentID: NSFileProviderUserInfoKey
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideruserinfokey/experimentid)*