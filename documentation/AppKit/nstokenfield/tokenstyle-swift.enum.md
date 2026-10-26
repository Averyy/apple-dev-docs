# NSTokenField.TokenStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The NSTokenStyle constants define how tokens are displayed and editable in the `NSTokenFieldCell`. These values are used by [`tokenStyle`](../nstokenfieldcell/tokenstyle.md) and the delegate method [`tokenFieldCell(_:styleForRepresentedObject:)`](../nstokenfieldcelldelegate/tokenfieldcell%28_,styleforrepresentedobject%29.md).

**Availability**:
- macOS

## Declaration

```swift
enum TokenStyle
```

```c
enum NSTokenStyle : NSUInteger;
```

## Topics

### Enumeration Cases
- [NSTokenField.TokenStyle.default](./tokenstyle-swift.enum/default.md)
- [NSTokenField.TokenStyle.none](./tokenstyle-swift.enum/none.md)
- [NSTokenField.TokenStyle.plainSquared](./tokenstyle-swift.enum/plainsquared.md)
- [NSTokenField.TokenStyle.rounded](./tokenstyle-swift.enum/rounded.md)
- [NSTokenField.TokenStyle.squared](./tokenstyle-swift.enum/squared.md)
### Initializers
- [init?(rawValue: UInt)](./tokenstyle-swift.enum/init%28rawvalue%29.md)
### Deprecated
- [NSDefaultTokenStyle](../nsdefaulttokenstyle.md)
  Style best used for keyword type tokens.
- [NSPlainTextTokenStyle](../nsplaintexttokenstyle.md)
  Style to use for data you want represented as plain-text and without any token background.
- [NSRoundedTokenStyle](../nsroundedtokenstyle.md)
  Style best used for address type tokens.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfield/tokenstyle-swift.enum)*