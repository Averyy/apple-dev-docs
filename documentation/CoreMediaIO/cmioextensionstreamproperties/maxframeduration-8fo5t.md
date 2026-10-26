# maxFrameDuration

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The maximum duration of a frame.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
@property (atomic, strong, nullable) NSDictionary * maxFrameDuration;
```

#### Discussion

The dictionary needs to represent a [`CMTime`](../../CoreMedia/cmtime.md) value that aligns with the frame duration of the current active format.

The key for this property is [`streamMaxFrameDuration`](../cmioextensionproperty/streammaxframeduration.md).

## See Also

### Configuring Source Properties
- [activeFormatIndex](./activeformatindex-8czm7.md)
  The index of the active format.
- [frameDuration](./frameduration-lrfi.md)
  A dictionary representation of a frame duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/maxframeduration-8fo5t)*