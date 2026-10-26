# frameDuration

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A dictionary representation of a frame duration.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
@property (atomic, strong, nullable) NSDictionary * frameDuration;
```

#### Discussion

The dictionary represents a [`CMTime`](../../CoreMedia/cmtime.md) value that’s consistent with the frame duration that the current active format specifies.

The key for this property is [`streamFrameDuration`](../cmioextensionproperty/streamframeduration.md).

## See Also

### Configuring Source Properties
- [activeFormatIndex](./activeformatindex-8czm7.md)
  The index of the active format.
- [maxFrameDuration](./maxframeduration-8fo5t.md)
  The maximum duration of a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/frameduration-lrfi)*