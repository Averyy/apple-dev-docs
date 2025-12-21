# Setting load and store actions

**Framework**: Metal

Set actions that define how a render pass loads and stores a render target.

#### Overview

[`MTLLoadAction`](mtlloadaction.md) and [`MTLStoreAction`](mtlstoreaction.md) values allow you to define how a render pass loads and stores your [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) objects. By choosing appropriate actions for your render targets, you can avoid costly and unnecessary work at the start (load) or end (store) of a render pass.

Set a render targetʼs texture on its [`texture`](mtlrenderpassattachmentdescriptor/texture.md) property. Then, set its actions on its [`loadAction`](mtlrenderpassattachmentdescriptor/loadaction.md) and [`storeAction`](mtlrenderpassattachmentdescriptor/storeaction.md) properties:

##### Choose a Load Action

Several options are available, depending on which of the following scenarios describes your render targetʼs loading needs.

 Choose [`MTLLoadAction.dontCare`](mtlloadaction/dontcare.md). This action incurs no cost, and pixel values are always undefined at the start of the render pass.

![A block diagram that shows the previous contents of a render target and its loaded contents after a Don’t Care load action.](https://docs-assets.developer.apple.com/published/7cbe7d6210b0c950a2e64ee927f1cf3b/media-3174626%402x.png)

 Choose [`MTLLoadAction.clear`](mtlloadaction/clear.md). This action incurs the cost of writing the render targetʼs clear value to each pixel.

![A block diagram that shows the previous contents of a render target and its loaded contents after a Clear load action.](https://docs-assets.developer.apple.com/published/cc14d2ba5f3ba032a79daa39c2131125/media-3174625%402x.png)

 Choose [`MTLLoadAction.load`](mtlloadaction/load.md). This action incurs the cost of loading the previous values of each pixel from memory. This action is significantly slower than [`MTLLoadAction.dontCare`](mtlloadaction/dontcare.md) or [`MTLLoadAction.clear`](mtlloadaction/clear.md).

![A block diagram that shows the previous contents of a render target and its loaded contents after a Load load action.](https://docs-assets.developer.apple.com/published/d46146edb2f07bd96ccd8cb2a93b51d2/media-3174621%402x.png)

> **Note**:  You canʼt choose [`MTLLoadAction.load`](mtlloadaction/load.md) for a memoryless render target because it isnʼt backed by system memory. For more information about memoryless render targets, see [`Choosing a resource storage mode for Apple GPUs`](choosing-a-resource-storage-mode-for-apple-gpus.md).

##### Choose a Store Action

Several options are available, depending on which of the following scenarios describes your render targetʼs storage needs.

 Choose [`MTLStoreAction.dontCare`](mtlstoreaction/dontcare.md). This action incurs no cost, and pixel values are always undefined at the end of the render pass. Choose this action for intermediary render targets that you use within the render pass, but you donʼt need afterward. This is typically the correct action for depth and stencil render targets.

![A block diagram that shows the previous contents of a render target and its stored contents after a Don’t Care store action.](https://docs-assets.developer.apple.com/published/41f424b40ac240d00812b4718c0f1160/media-3174628%402x.png)

 Choose [`MTLStoreAction.store`](mtlstoreaction/store.md). This action incurs the cost of storing the values of each pixel to memory. This is always the correct action for drawables.

![A block diagram that shows the previous contents of a render target and its stored contents after a Store store action.](https://docs-assets.developer.apple.com/published/85088cb54304cfe0edef050dd5a1c742/media-3174627%402x.png)

 When you perform multisampling, you decide whether to store the render targetʼs multisampled or resolved data. Multisampled data is stored in the render targetʼs [`texture`](mtlrenderpassattachmentdescriptor/texture.md) property. Resolved data is stored in the render targetʼs [`resolveTexture`](mtlrenderpassattachmentdescriptor/resolvetexture.md) property. Refer to this table to choose a store action when multisampling:

| Multisampled data stored | Resolved data stored | Resolve texture required | Required store action |
| --- | --- | --- | --- |
| Yes | Yes | Yes | [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md) |
| Yes | No | No | [`MTLStoreAction.store`](mtlstoreaction/store.md) |
| No | Yes | Yes | [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md) |
| No | No | No | [`MTLStoreAction.dontCare`](mtlstoreaction/dontcare.md) |

To store and resolve a multisample texture in a single render pass, always choose the [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md) action and use a single render command encoder.

 In some cases, you might not know which store action to use for a particular render target until you gather more render pass information. To defer your store action choice, set the temporary [`MTLStoreAction.unknown`](mtlstoreaction/unknown.md) value when you create your [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md) object. Setting an unknown store action may avoid potential costs incurred by setting another store action prematurely. However, you need to specify a valid store action before you finish encoding your render pass; otherwise, an error occurs.

> **Note**:  You canʼt choose [`MTLStoreAction.store`](mtlstoreaction/store.md) or [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md) for a memoryless render target because it isnʼt backed by system memory. For more information about memoryless render targets, see [`Choosing a resource storage mode for Apple GPUs`](choosing-a-resource-storage-mode-for-apple-gpus.md).

##### Evaluate Actions Between Render Passes

You can use the same render targets across multiple render passes. Several load and store combinations are possible for the same render target between any two render passes, depending on which of the following scenarios describes your render targetʼs needs from one render pass to another.

 In the first render pass, choose [`MTLStoreAction.dontCare`](mtlstoreaction/dontcare.md) to avoid storing the contents of the render target. In the second render pass, choose [`MTLLoadAction.dontCare`](mtlloadaction/dontcare.md) or [`MTLLoadAction.clear`](mtlloadaction/clear.md) to avoid loading the contents of the render target.

![A block diagram that shows a store and load sequence for a single render target. The render target uses a Don’t Care store action and a Don’t Care load action.](https://docs-assets.developer.apple.com/published/194bfae826cd6005bd66aa17d5d7a29a/media-3174622%402x.png)

![A block diagram that shows a store and load sequence for a single render target. The render target uses a Don’t Care store action and a Clear load action.](https://docs-assets.developer.apple.com/published/37cea4d54747a07c9abc09a62b25761c/media-3174623%402x.png)

 In the first render pass, choose [`MTLStoreAction.store`](mtlstoreaction/store.md), [`MTLStoreAction.multisampleResolve`](mtlstoreaction/multisampleresolve.md), or [`MTLStoreAction.storeAndMultisampleResolve`](mtlstoreaction/storeandmultisampleresolve.md) to store the contents of the render target. In the second render pass, choose [`MTLLoadAction.load`](mtlloadaction/load.md) to load the contents of the render target.

![A block diagram that shows a store and load sequence for a single render target. The render target uses a Store, Multisample Resolve, or Store And Multisample Resolve store action, and then uses a Load load action.](https://docs-assets.developer.apple.com/published/0909b9c8f011dff122de8ecbb7208c80/media-3174624%402x.png)

## See Also

- [Drawing a triangle with Metal 4](drawing-a-triangle-with-metal-4.md)
  Render a colorful, rotating 2D triangle by running draw commands with a render pipeline on a GPU.
- [Customizing render pass setup](customizing-render-pass-setup.md)
  Render into an offscreen texture by creating a custom render pass.
- [Improving rendering performance with vertex amplification](improving-rendering-performance-with-vertex-amplification.md)
  Run draw commands that render to different outputs using the same vertex data multiple times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/setting-load-and-store-actions)*