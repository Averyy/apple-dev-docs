# maximumRetries

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The maximum number of retries.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var maximumRetries: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger maximumRetries;
```

## Discussion

You can specify up to 256 retries. By default, the value of this parameter is `0`.

## See Also

### Configuring a Tag Command
- [var retryInterval: TimeInterval](./retryinterval.md)
  The time between retries, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctagcommandconfiguration/maximumretries)*