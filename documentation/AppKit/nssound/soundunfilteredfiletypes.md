# soundUnfilteredFileTypes

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Provides the list of file types the [`NSSound`](../nssound.md) class understands.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`name`](./name-swift.property.md).

## Declaration

```objc
+ (NSArray *) soundUnfilteredFileTypes;
```

#### Return Value

Array of strings representing the file types the [`NSSound`](../nssound.md) class understands.

#### Discussion

The returned array may be passed directly to the [`runModalForTypes:`](../nsopenpanel/runmodalfortypes_.md) method of the  [`NSOpenPanel`](../nsopenpanel.md) class.

## See Also

### Deprecated
- [- channelMapping](./channelmapping.md)
  Provides the receiver’s channel map.
- [- setChannelMapping:](./setchannelmapping_.md)
  Specifies the receiver’s channel map.
- [+ soundUnfilteredPasteboardTypes](./soundunfilteredpasteboardtypes.md)
  Provides a list of the pasteboard types that the `NSSound` class can accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/soundunfilteredfiletypes)*