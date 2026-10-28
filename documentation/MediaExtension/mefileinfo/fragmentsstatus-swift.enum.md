# MEFileInfo.FragmentsStatus

**Framework**: MediaExtension  
**Kind**: enum  
**Role**: Enumeration

An enumeration that describes if a media asset contains or supports fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum FragmentsStatus
```

```c
enum MEFileInfoFragmentsStatus : NSInteger;
```

## Overview

For QuickTime movie and ISO files, it indicates the presence of an `mvex` box, which is necessary to signal the possible presence of later `moof` boxes.

## Topics

### File fragment status values
- [MEFileInfo.FragmentsStatus.couldNotContainFragments](./fragmentsstatus-swift.enum/couldnotcontainfragments.md)
  The file isn’t extendable by fragments.
- [MEFileInfo.FragmentsStatus.containsFragments](./fragmentsstatus-swift.enum/containsfragments.md)
  The file is extendable by fragments and contains at least one fragment.
- [MEFileInfo.FragmentsStatus.couldContainButDoesNotContainFragments](./fragmentsstatus-swift.enum/couldcontainbutdoesnotcontainfragments.md)
  The file is extendable by fragments, but doesn’t contain any fragments.
- [MEFileInfo.FragmentsStatus.couldNotContainFragments](./fragmentsstatus-swift.enum/couldnotcontainfragments.md)
  The file isn’t extendable by fragments.
- [MEFileInfo.FragmentsStatus.containsFragments](./fragmentsstatus-swift.enum/containsfragments.md)
  The file is extendable by fragments and contains at least one fragment.
- [MEFileInfo.FragmentsStatus.couldContainButDoesNotContainFragments](./fragmentsstatus-swift.enum/couldcontainbutdoesnotcontainfragments.md)
  The file is extendable by fragments, but doesn’t contain any fragments.
### Initializers
- [init?(rawValue: Int)](./fragmentsstatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting file properties
- [var duration: CMTime](./duration.md)
  The duration of the media asset, if available.
- [var fragmentsStatus: MEFileInfo.FragmentsStatus](./fragmentsstatus-swift.property.md)
  Indicates if the media asset contains fragments or is extendable by fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/fragmentsstatus-swift.enum)*