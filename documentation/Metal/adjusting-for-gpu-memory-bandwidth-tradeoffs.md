# Adjusting for GPU Memory Bandwidth Tradeoffs

**Framework**: Metal

Choose a suitable GPU and memory storage mode for tasks based on that GPU’s memory bandwidth on a Mac.

#### Overview

GPU memory  is a measure of the data transfer speed between a GPU and the system across a bus, such as PCI Express (PCIe) or Thunderbolt. It’s important to consider the bandwidth of each GPU in a system when developing your high-performance Metal apps. A GPU that’s powerful on its own may not be the optimal choice for certain tasks if it has a relatively low bandwidth connection to the system.

##### Consider How a Gpu Connects to the System

A GPU’s bandwidth largely depends on the bus that connects it to a system:

- An  GPU connects to a system though an external Thunderbolt 3 bus.
- A  GPU is a built-in GPU that has video memory (separate memory that only the GPU can access) and connects to a system through an internal PCIe bus.
- An  GPU is a built-in GPU that uses system memory and shares the bus with the CPU.

![A system diagram that shows an iMac Pro and its connections to both a built-in discrete GPU and an external GPU. The discrete GPU connects to the iMac through an internal PCIe bus, and the external GPU connects through an external Thunderbolt 3 bus.](https://docs-assets.developer.apple.com/published/83c1259137eebf0aa4587150be955e6b/media-4085591%402x.png)

A discrete GPU’s PCIe bus can have 8 or 16 memory lanes — or PCIe x4 or PCIe x16, respectively — depending on the GPU and Mac model. Transferring data between the system and an external GPU can take more time than with a built-in GPU because external GPUs typically have a lower bandwidth connection, such as Thunderbolt 3.

![A horizontal bar chart that shows the relative bandwidths of Thunderbolt 3 (1x), PCIe with 8 lanes (2x), and PCIe with 16 lanes (4x).](https://docs-assets.developer.apple.com/published/94b6398aae2e8085a01a628a2dd31fa3/media-4085592%402x.png)

Additionally, transferring data from one GPU to another can be even more expensive because the system can’t transfer data directly between GPUs. Instead, the process typically requires copying data to system memory before copying it again to the destination GPU.

##### Select the Appropriate Storage Mode for Your Resources

You can minimize the bandwidth costs — the number of data transfers across a bus — by selecting an appropriate storage mode for your app’s resources. For more information about selecting a storage mode for specific GPUs, see [`Choosing a Resource Storage Mode for Apple GPUs`](choosing-a-resource-storage-mode-for-apple-gpus.md) and [`Choosing a Resource Storage Mode for Intel and AMD GPUs`](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md). Metal uses a resource’s storage mode to determine which memory location to save it in. The storage mode options for a resource include the following:

Discrete and external GPUs have the highest data transfer costs when they access a shared resource because their access to system memory is relatively slow.

![A system diagram that doesn’t recommend a setup where a discrete GPU and an external GPU each store a shared resource in system memory instead of in their dedicated video memory (discrete and external memory, respectively) over a direct, fast connection. Both GPUs and the CPU can access system memory, and the other GPU’s resource, through different connections: The discrete GPU connects through an internal PCIe connection, the external GPU connects through an external Thunderbolt 3 connection, and the CPU connects directly to system memory.](https://docs-assets.developer.apple.com/published/28a42da176d4d3bb0248d39afaaa00cc/media-2960167%402x.png)

Private resources have the lowest data transfer costs with discrete and external GPUs because their exclusive access to video memory is relatively fast.

![A system diagram that recommends a setup where a discrete GPU and an external GPU each store a private resource both in their dedicated video memory (discrete and external memory, respectively) over a direct, fast connection. Both GPUs and the CPU can access system memory through different connections: The discrete GPU connects through an internal PCIe connection, the external GPU connects through an external Thunderbolt 3 connection, and the CPU connects directly to system memory.](https://docs-assets.developer.apple.com/published/a48c90fa5d180d5d33e5fd95c8562847/media-2960169%402x.png)

Managed resources can have modest data transfer costs for discrete and external GPUs. The CPU (and an integrated GPU) have quick access to the copy in system memory, and the other GPUs have quick access to the copy in their video memory.

![A system diagram that recommends a setup where a discrete GPU and an external GPU each store a managed resource both in its dedicated video memory (discrete and external, respectively) over a direct, fast connection, and in system memory. Both GPUs and the CPU can access system memory through different connections: The discrete GPU connects through an internal PCIe connection, the external GPU connects through an external Thunderbolt 3 connection, and the CPU connects directly to system memory. Each GPU can access the other GPU’s managed resource by using the system memory’s copy of that resource.](https://docs-assets.developer.apple.com/published/b01c231495f1bdcdf4d0af58141c56e6/media-4085392%402x.png)

You can keep the copies in sync by efficiently running sparse blit operations (see [`Synchronizing a Managed Resource in macOS`](synchronizing-a-managed-resource-in-macos.md)).

##### Render a Drawable on the Same Gpu That Drives the Destination Display

In Metal, a , represented by [`MTLDrawable`](mtldrawable.md), is a type that bridges Metal and [`Core Animation`](https://developer.apple.com/documentation/QuartzCore). Each drawable contains a texture that your apps can render with Metal and then present on a device’s display using Core Animation.

Presenting a drawable on a display can have significant bandwidth costs if the drawable belongs to a GPU that doesn’t drive the display. Only one GPU can drive a display, whether it’s built in or external, and the fastest path to present a drawable to a display is to render that drawable with the same GPU that drives the display. Otherwise, the system has to transfer the drawable from the GPU that renders it to the GPU that drives the display.

For example, take a Mac that has both a discrete GPU and an external GPU that’s driving an external display. If your app renders a drawable with the discrete GPU, the system has to transfer the drawable to the external GPU through the Thunderbolt 3 bus to present it on the external display. You app can avoid this transfer by rendering the drawable with the external GPU because it’s also driving the drawable’s destination display.

![A system diagram that shows two possible pathways for a drawable, starting from either the external GPU or the discrete GPU. The diagram recommends the pathway that uses the external GPU to render a drawable because it’s the same GPU that’s driving the external display. The diagram discourages rendering a drawable with the discrete GPU when the external GPU is driving the display because that forces the system to transfer each drawable over the Thunderbolt 3 bus.](https://docs-assets.developer.apple.com/published/3c0705eb46bb14d072b6534e22ae1ff0/media-4085391%402x.png)

Similarly, Mac systems with multiple built-in GPUs may need to transfer a drawable that one GPU renders if a different GPU drives the destination display. For example, imagine a MacBook Pro with automatic graphics switching is currently driving the built-in display with the integrated GPU. If your app uses the discrete GPU to render a drawable, the system has to transfer the drawable’s contents to the integrated GPU over the internal PCIe bus. Your app can avoid this transfer by rendering the drawable with the integrated GPU when it’s driving the internal display.

![A system diagram that shows two possible pathways for a drawable, starting from either the integrated GPU or the discrete GPU. The diagram recommends the pathway that uses the integrated GPU to render a drawable because its the same GPU that’s driving the built-in display. The diagram discourages rendering a drawable with the discrete GPU when the integrated GPU is driving the built-in display because that forces the system to transfer each drawable over the PCIe bus.](https://docs-assets.developer.apple.com/published/e2b8d38493c37785368e2efd35fa8578/media-4085390%402x.png)

## See Also

- [Assessing Multi-GPU and Multi-Display Setups on an Intel-Based Mac](assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac.md)
  Learn the possible GPU and display configurations for a Mac and their limitations.
- [Selecting Device Objects for Graphics Rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Selecting Device Objects for Compute Processing](selecting-device-objects-for-compute-processing.md)
  Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/adjusting-for-gpu-memory-bandwidth-tradeoffs)*