# AudioClassDescription

**Framework**: Core Audio Types  
**Kind**: struct

A structure that describes an audio codec.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioClassDescription
```

## Topics

### Accessing the Data
- [var mType: OSType](audioclassdescription/mtype.md)
  A four character code that a manufacturer defines for a codec type.
- [var mSubType: OSType](audioclassdescription/msubtype.md)
  A four character code that a manufacturer defines for a codec subtype.
- [var mManufacturer: OSType](audioclassdescription/mmanufacturer.md)
  A four character code that identifies a codec manufacturer.
### Initializers
- [init()](audioclassdescription/init.md)
  Creates an empty audio class description.
- [init(mType: OSType, mSubType: OSType, mManufacturer: OSType)](audioclassdescription/init(mtype:msubtype:mmanufacturer:).md)
  Creates an audio class description for the type, subtype, and manufacturer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audioclassdescription)*