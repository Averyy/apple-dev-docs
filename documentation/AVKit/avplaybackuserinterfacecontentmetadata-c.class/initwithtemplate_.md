# initWithTemplate:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new metadata object by copying values from a metadata template.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (instancetype) initWithTemplate:(AVPlaybackUserInterfaceContentMetadataTemplate *) metadataTemplate;
```

#### Discussion

This initializer creates an immutable [`AVPlaybackUserInterfaceContentMetadata`](../avplaybackuserinterfacecontentmetadata-c.class.md) instance from a mutable [`AVPlaybackUserInterfaceContentMetadataTemplate`](../avplaybackuserinterfacecontentmetadatatemplate.md), providing a convenient way to convert configured template data into stable metadata for playback interfaces.

All properties from the template are copied into the new metadata object, creating an independent immutable snapshot of the template’s current state. Subsequent changes to the template will not affect the created metadata object.

## Parameters

- `metadataTemplate`: The metadata template to copy values from. If `nil`, returns a metadata object with default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithtemplate:)*