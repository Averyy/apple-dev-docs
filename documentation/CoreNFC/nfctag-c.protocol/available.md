# available

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a detected tag is available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```objc
@property (nonatomic, readonly, getter=isAvailable) BOOL available;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the tag is available in the current reader session. When a tag is removed from an RF field, it becomes unavailable.

## See Also

### Getting Information About a Tag
- [session](./session.md)
  The reader session that provides the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfctag-c.protocol/available)*