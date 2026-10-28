# OSLogMessageComponent.ArgumentCategory

**Framework**: OSLog  
**Kind**: enum  
**Role**: Enumeration

The data type corresponding to the argument provided in a message payload.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum ArgumentCategory
```

```c
enum OSLogMessageComponentArgumentCategory : NSInteger;
```

## Overview

For example, `OSLogMessageComponent` can represent the number associated with a `%d` placeholder. This value can be undefined if the argument data cann’t be decoded, for example if it were redacted.

## Topics

### Constants
- [OSLogMessageComponent.ArgumentCategory.data](./argumentcategory-swift.enum/data.md)
  The argument is an [`NSData`](../../Foundation/nsdata.md) object.
- [OSLogMessageComponent.ArgumentCategory.double](./argumentcategory-swift.enum/double.md)
  The argument is a double.
- [OSLogMessageComponent.ArgumentCategory.int64](./argumentcategory-swift.enum/int64.md)
  The argument is a 64-bit signed integer.
- [OSLogMessageComponent.ArgumentCategory.string](./argumentcategory-swift.enum/string.md)
  The argument is a string.
- [OSLogMessageComponent.ArgumentCategory.uInt64](./argumentcategory-swift.enum/uint64.md)
  The argument is a 64-bit unsigned integer.
- [OSLogMessageComponent.ArgumentCategory.undefined](./argumentcategory-swift.enum/undefined.md)
  The argument’s type is not defined.
### Initializers
- [init?(rawValue: Int)](./argumentcategory-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading the Argument
- [var argument: OSLogMessageComponent.Argument](./argument-swift.property.md)
  The argument passed into the message component.
- [OSLogMessageComponent.Argument](./argument-swift.enum.md)
  An object representing data that corresponds to an argument in a message payload.
- [var argumentCategory: OSLogMessageComponent.ArgumentCategory](./argumentcategory-swift.property.md)
  The type of argument that corresponds to the placeholder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogmessagecomponent/argumentcategory-swift.enum)*