# Storing data a pass makes with custom sample positions for a subsequent pass

**Framework**: Metal

Inform Metal when your app uses programmable sample positions for its depth render targets or copies MSAA depth data.

#### Overview

A render or compute pass usually stores its target’s depth data in a compressed format. Any subsequent pass has to use the correct sample positions to decompress the data before reading it. You can store depth data in a representation that uses arbitrary sample positions (see [`Positioning samples programmatically`](positioning-samples-programmatically.md)).

> ❗ **Important**:  You can sample depth positions programmatically only on devices that support programmable sample positions (see [`areProgrammableSamplePositionsSupported`](mtldevice/areprogrammablesamplepositionssupported.md)).

When your app uses custom sampling positions, inform Metal by setting the [`MTLRenderPassColorAttachmentDescriptor`](mtlrenderpasscolorattachmentdescriptor.md) or [`MTLRenderPassDepthAttachmentDescriptor`](mtlrenderpassdepthattachmentdescriptor.md) instance’s [`storeActionOptions`](mtlrenderpassattachmentdescriptor/storeactionoptions.md) property to [`customSamplePositions`](mtlstoreactionoptions/customsamplepositions.md). This setting tells Metal that any subsequent pass that reads the attachment may not know the sample positions the current pass uses to generate the data. Examples of a pass that can use custom sample positions include the following:

- A fragment shader that uses unique, programmable sample positions
- A blit pass that copies MSAA depth data to another resource

In this scenario, Metal may decompress the depth render target and store the uncompressed data.

> 💡 **Tip**:  Improve the performance of a pass if its programmable sample positions are the same for the next pass by setting the descriptor’s [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) property to [`MTLStoreAction.store`](mtlstoreaction/store.md) and clearing the [`customSamplePositions`](mtlstoreactionoptions/customsamplepositions.md) option from the [`storeActionOptions`](mtlrenderpassattachmentdescriptor/storeactionoptions.md) property.

## See Also

- [Positioning samples programmatically](positioning-samples-programmatically.md)
  Configure the position of samples when rendering to a multisampled render target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/storing-data-a-pass-makes-with-custom-sample-positions-for-a-subsequent-pass)*