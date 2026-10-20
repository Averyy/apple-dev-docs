# isSupported

**Framework**: Core NFC  
**Kind**: property  
**Role**: Type Property

A property that indicates whether the current device supports card session functionality.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class var isSupported: Bool { get }
```

#### Discussion

Query this property before calling [`init()`](./init%28%29.md) to avoid raising [`fatalError(_:file:line:)`](../../Swift/fatalerror%28_,file,line%29.md) on ineligible devices.

## See Also

### Determining card session availability
- [static var isEligible: Bool](./iseligible.md)
  A property that indicates whether the current system supports card session functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/issupported)*