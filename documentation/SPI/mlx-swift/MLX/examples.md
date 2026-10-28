---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/examples"
framework: "mlx-swift/MLX"
---

# MLX Swift Examples

**Framework**: mlx-swift/MLX  
**Role**: Sample Code  
**Download**: [main.zip](https://github.com/ml-explore/mlx-swift-examples/archive/refs/heads/main.zip)

Swift example code for MLX and MLXNN.

## Overview

Examples using [MLX](./MLX.md) and `MLXNN` are available in [mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples) (example applications and tools) and [mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm) (implementations of various LLM and VLM model architectures). The examples include:

- [MNISTTrainer](https://github.com/ml-explore/mlx-swift-examples/blob/main/Applications/MNISTTrainer/README.md): An example that runs on both iOS and macOS that downloads MNIST training data and trains a [LeNet](https://en.wikipedia.org/wiki/LeNet).
- [MLXChatExample](https://github.com/ml-explore/mlx-swift-examples/blob/main/Applications/MLXChatExample/README.md): An example chat app that runs on both iOS and macOS that supports LLMs and VLMs.
- [LLMEval](https://github.com/ml-explore/mlx-swift-examples/blob/main/Applications/LLMEval/README.md): A simple example that runs on both iOS and macOS that downloads an LLM and tokenizer from Hugging Face and generates text from a given prompt.
- [StableDiffusionExample](https://github.com/ml-explore/mlx-swift-examples/blob/main/Applications/StableDiffusionExample/README.md): An example that runs on both iOS and macOS that downloads a stable diffusion model from Hugging Face and generates an image from a given prompt.
- [llm-tool](https://github.com/ml-explore/mlx-swift-examples/blob/main/Tools/llm-tool/README.md): A command line tool for generating text using a variety of LLMs available on the Hugging Face hub.

and several more.  Much of the code is also available as a SwiftPM package – use this as a starting point to build your own applications.

## See Also

### MLX
- [Installation](./install.md)
  How to install and use.
- [Troubleshooting](./troubleshooting.md)
  Help with problems you might run into.
- [Converting From Python](./converting-python.md)
  Common patterns from python and mapping `mlx` function names.
- [Numpy Style Broadcasting](./broadcasting.md)
  How different size arrays can be used together.
- [Lazy Evaluation](./lazy-evaluation.md)
  Computation in `MLX` is lazy.  Understand when the graph is evaluated.
- [Unified Memory](./unified-memory.md)
  `MLX` takes advantage of the shared memory between the CPU and GPU.
- [Vectorization](./vmap.md)
  Automatic vectorization with `vmap`.
- [Compilation](./compilation.md)
  MLX has a [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) function transformation which compiles computation graphs. Function compilation results in smaller graphs by merging common work and fusing certain operations. In many cases this can lead to big improvements in run-time and memory use.
- [Using Streams](./using-streams.md)
  Controlling where your computations are evaluated.
- [Running on iOS](./running-on-ios.md)
  Considerations for running on iOS and general memory tuning.
- [Wired Memory Management](./wired-memory.md)
  Coordinate a process-wide wired memory limit for GPU workloads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/examples)*