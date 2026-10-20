# instanceID

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The unique, persistent identifier of this token that the token implementation creates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var instanceID: TKToken.InstanceID { get }
```

```objc
@property (nonatomic, readonly) TKTokenInstanceID instanceID;
```

#### Discussion

The instance identifier often represents some kind of serial number of the target hardware.

## See Also

### Reporting Configuration Information
- [var configurationData: Data?](./configurationdata.md)
  Additional configuration information for the token instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class/instanceid)*