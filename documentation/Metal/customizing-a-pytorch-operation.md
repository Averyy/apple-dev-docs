# Customizing a PyTorch operation

**Framework**: Metal

Implement a custom operation in PyTorch that uses Metal kernels to improve performance.

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10050: [`Optimize machine learning for Metal apps`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10050).

##### Configure the Sample Code Project

Before you run the sample code project:

1. Follow the instructions in [`Accelerated PyTorch training on Mac`](https://developer.apple.comhttps://developer.apple.com/metal/pytorch/).
2. Install PyTorch nightly (Python 3.7 or later is required). ```shell
pip3 install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu
```
3. Install Ninja ```shell
pip3 install Ninja
```
4. Run the sample. ```shell
python3 run_sample.py
```

## See Also

- [Performing Calculations on a GPU](performing-calculations-on-a-gpu.md)
  Use Metal to find GPUs and perform calculations on them.
- [Selecting Device Objects for Compute Processing](selecting-device-objects-for-compute-processing.md)
  Switch dynamically between multiple GPUs to efficiently execute a compute-intensive simulation.
- [Customizing a TensorFlow operation](customizing-a-tensorflow-operation.md)
  Implement a custom operation that uses Metal kernels to accelerate neural-network training performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Metal/customizing-a-pytorch-operation)*