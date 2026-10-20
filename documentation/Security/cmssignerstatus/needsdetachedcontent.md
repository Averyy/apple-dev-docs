# CMSSignerStatus.needsDetachedContent

**Framework**: Security  
**Kind**: case  
**Role**: Case

The message was signed but has detached content. You must call the [`CMSDecoderSetDetachedContent(_:_:)`](../cmsdecodersetdetachedcontent%28_,_%29.md) function before ascertaining the signature status.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case needsDetachedContent
```

```c
kCMSSignerNeedsDetachedContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmssignerstatus/needsdetachedcontent)*