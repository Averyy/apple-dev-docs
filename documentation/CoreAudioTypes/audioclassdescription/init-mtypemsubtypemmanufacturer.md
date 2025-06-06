# init(mType:mSubType:mManufacturer:)

**Framework**: Core Audio Types  
**Kind**: init

Creates an audio class description for the type, subtype, and manufacturer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mType: OSType, mSubType: OSType, mManufacturer: OSType)
```

## Parameters

- `mType`: A four character code that a manufacturer defines for a codec type.
- `mSubType`: A four character code that a manufacturer defines for a codec subtype.
- `mManufacturer`: A four character code that identifies a codec manufacturer.

## See Also

- [init()](audioclassdescription/init.md)
  Creates an empty audio class description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audioclassdescription/init(mtype:msubtype:mmanufacturer:))*