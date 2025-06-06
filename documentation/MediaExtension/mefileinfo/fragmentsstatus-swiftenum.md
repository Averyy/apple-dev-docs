# MEFileInfo.FragmentsStatus

**Framework**: MediaExtension  
**Kind**: enum

An enumeration that describes if a media asset contains or supports fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum FragmentsStatus
```

#### Overview

For QuickTime movie and ISO files, it indicates the presence of an `mvex` box, which is necessary to signal the possible presence of later `moof` boxes.

## Topics

### File fragment status values
- [MEFileInfo.FragmentsStatus.couldNotContainFragments](mefileinfo/fragmentsstatus-swift.enum/couldnotcontainfragments.md)
  The file isn’t extendable by fragments.
- [MEFileInfo.FragmentsStatus.containsFragments](mefileinfo/fragmentsstatus-swift.enum/containsfragments.md)
  The file is extendable by fragments and contains at least one fragment.
- [MEFileInfo.FragmentsStatus.couldContainButDoesNotContainFragments](mefileinfo/fragmentsstatus-swift.enum/couldcontainbutdoesnotcontainfragments.md)
  The file is extendable by fragments, but doesn’t contain any fragments.
- [MEFileInfo.FragmentsStatus.couldNotContainFragments](mefileinfo/fragmentsstatus-swift.enum/couldnotcontainfragments.md)
  The file isn’t extendable by fragments.
- [MEFileInfo.FragmentsStatus.containsFragments](mefileinfo/fragmentsstatus-swift.enum/containsfragments.md)
  The file is extendable by fragments and contains at least one fragment.
- [MEFileInfo.FragmentsStatus.couldContainButDoesNotContainFragments](mefileinfo/fragmentsstatus-swift.enum/couldcontainbutdoesnotcontainfragments.md)
  The file is extendable by fragments, but doesn’t contain any fragments.
### Initializers
- [init?(rawValue: Int)](mefileinfo/fragmentsstatus-swift.enum/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](mefileinfo/fragmentsstatus-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](mefileinfo/fragmentsstatus-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var duration: CMTime](mefileinfo/duration.md)
  The duration of the media asset, if available.
- [var fragmentsStatus: MEFileInfo.FragmentsStatus](mefileinfo/fragmentsstatus-swift.property.md)
  Indicates if the media asset contains fragments or is extendable by fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mefileinfo/fragmentsstatus-swift.enum)*