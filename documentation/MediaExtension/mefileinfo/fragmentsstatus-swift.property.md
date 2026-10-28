# fragmentsStatus

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Indicates if the media asset contains fragments or is extendable by fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var fragmentsStatus: MEFileInfo.FragmentsStatus { get set }
```

```objc
@property (nonatomic) MEFileInfoFragmentsStatus fragmentsStatus;
```

## Discussion

The default value is [`MEFileInfo.FragmentsStatus.couldNotContainFragments`](./fragmentsstatus-swift.enum/couldnotcontainfragments.md).

## See Also

### Inspecting file properties
- [var duration: CMTime](./duration.md)
  The duration of the media asset, if available.
- [MEFileInfo.FragmentsStatus](./fragmentsstatus-swift.enum.md)
  An enumeration that describes if a media asset contains or supports fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/fragmentsstatus-swift.property)*