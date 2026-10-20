# retryInterval

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The time between retries, in seconds.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var retryInterval: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval retryInterval;
```

#### Discussion

By default, the value of this parameter is `0`.

## See Also

### Configuring a Tag Command
- [var maximumRetries: Int](./maximumretries.md)
  The maximum number of retries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagcommandconfiguration/retryinterval)*