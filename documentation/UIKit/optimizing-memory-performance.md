# Optimizing memory performance

**Framework**: UIKit

Measure the impact of the 64-bit runtime on your app’s memory usage.

#### Overview

The 64-bit runtime increases the size of pointers and some scalar data, resulting in a larger memory footprint for your app. The result is increased pressure on processor caches and virtual memory, which can adversely affect performance. When developing a 64-bit app, it’s critical to profile and optimize your app’s memory usage.

##### Test and Profile Your App

Start by creating standard tests to run against the 64-bit version of your app. With these tests, you can measure the penalty for compiling a 64-bit version of your app when compared with the 32-bit version. You can also measure improvements as you optimize your app’s memory usage.

For at least one test, use a minimal footprint — for example, one in which the app has just been opened and shows an empty document. For other tests, use a variety of data sizes, including at least one test with a very large data set. A complex app may require multiple sets of test data, each covering a subset of the app’s features.

The goal of these tests is to measure whether memory usage varies as the type or amount of data changes. If a particular kind of data causes the 64-bit version of your app to use dramatically more memory than the original 32-bit version, that’s a likely place to find opportunities for improvements.

##### Use the Correct Function to Get the Virtual Memory Page Size

Most apps don’t need to know the size of a virtual memory page, but some use it for buffer allocations and framework calls. The page size may vary between devices, so always use the `getpagesize()` function to get the size of the page.

##### Ensure That Your Code Is Position Independent

The 64-bit runtime environment supports only position-independent executables (PIE). By default, most apps are position independent. If some factor, such as a statically linked library or assembly code, is preventing your app from building as a PIE, you need to update your code when porting your app to the 64-bit runtime.

## See Also

- [Verifying mathematical calculations](verifying-mathematical-calculations.md)
  Ensure the accuracy of your math operations in 64-bit architecture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/optimizing-memory-performance)*