# Assessing Multi-GPU and Multi-Display Setups on an Intel-Based Mac

**Framework**: Metal

Learn the possible GPU and display configurations for a Mac and their limitations.

#### Overview

An Intel-based Mac can have multiple GPUs, and each GPU may connect to zero, one, or multiple displays. Prepare your app for various combinations of GPUs and display configurations by testing as many as possible, starting with the more common ones described below.

![An image that shows a single MacBook Pro, three overlapping, external GPUs, and two overlapping, external displays.](https://docs-assets.developer.apple.com/published/c776350aeeab804a826997bf07e005f0/media-2959797%402x.png)

In general, each GPU in the system has its advantages and tradeoffs, depending on your app’s needs. It’s important your app chooses an appropriate GPU for each task, especially when it involves presenting the results on a specific display or transferring data between GPUs. For more information about choosing GPUs and transferring data between them, see [`Finding Multiple GPUs on an Intel-based Mac`](finding-multiple-gpus-on-an-intel-based-mac.md) and [`Adjusting for GPU Memory Bandwidth Tradeoffs`](adjusting-for-gpu-memory-bandwidth-tradeoffs.md).

> 💡 **Tip**:  As an alternative to implementing a policy that selects a GPU and a display for a task, your app can suggest configurations to a person and let them decide.

 As an alternative to implementing a policy that selects a GPU and a display for a task, your app can suggest configurations to a person and let them decide.

##### Consider Various Gpu and Display Configurations

For a Mac with one built-in GPU — either integrated or discrete — that GPU always drives the built-in display.

![A system diagram that shows a MacBook Pro with a single, built-in GPU.](https://docs-assets.developer.apple.com/published/04f3eca6fb75e41ae37bdcf5defac6f7/media-2960165%402x.png)

For a Mac with two built-in GPUs — both an integrated GPU and a discrete GPU — either GPU can drive the built-in display.

![A system diagram that shows a MacBook Pro with two built-in GPUs.](https://docs-assets.developer.apple.com/published/b022119842cf3a4a9bc64718e4ac3a20/media-3993424%402x.png)

A Mac can also directly connect to and drive one or more external displays. For a Mac that has a single, built-in GPU (either integrated or discrete), that GPU drives every display that’s directly connected.

However, for a Mac with two built-in GPUs (both integrated and discrete), only the discrete GPU can drive the external displays. The discrete GPU also drives the built-in display when the Mac is driving one or more external displays. On that same Mac, the integrated GPU can drive only the built-in display, and only when the Mac isn’t driving any external displays.

![A system diagram that shows two external displays that connect to a MacBook Pro through separate connections.](https://docs-assets.developer.apple.com/published/efa16b8c347bd7c8298f23522e39838e/media-3993425%402x.png)

Your app can use external GPUs for compute or rendering tasks, but an external GPU can’t drive the built-in display.

![A system diagram that shows two external GPUs that connect to a MacBook Pro through separate, external connections.](https://docs-assets.developer.apple.com/published/48d37a14fcf9ce28e62e71ea938d9805/media-3993426%402x.png)

For a display that’s connected to an external GPU, only that GPU can drive the display. A built-in GPU can’t drive a display that’s connected to an external GPU.

![A system diagram that shows an external GPU that connects a MacBook Pro to an external display.](https://docs-assets.developer.apple.com/published/b22a3f95645c4220377c91079b7fb6c5/media-3993427%402x.png)

A person can configure a Mac with a combination of the scenarios above. For example, someone may connect multiple external GPUs and external displays that directly connect to the Mac and indirectly through an external GPU.

![A system diagram that shows an iMac Pro connected to an external display, an external GPU, and another external GPU that’s also connected to two additional external displays.](https://docs-assets.developer.apple.com/published/b505af846a78d0167e779ce702fb7d61/media-3993428%402x.png)

## See Also

- [Adjusting for GPU Memory Bandwidth Tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)
  Choose a suitable GPU and memory storage mode for tasks based on that GPU’s memory bandwidth on a Mac.
- [Selecting Device Objects for Graphics Rendering](selecting-device-objects-for-graphics-rendering.md)
  Switch dynamically between multiple GPUs to efficiently render to a display.
- [Selecting Device Objects for Compute Processing](selecting-device-objects-for-compute-processing.md)
  Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/assessing-multi-gpu-and-multi-display-setups-on-an-intel-based-mac)*