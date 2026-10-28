---
url: "https://docs.swift.org/latest/documentation/wasmguide/troubleshooting"
framework: "Swift-Org/WasmGuide"
---

# Troubleshooting

**Framework**: Swift-Org/WasmGuide  
**Role**: Article

These are some common issues you may run into while using Swift with WebAssembly.

## Overview

If you are having trouble that is not listed here, try searching for it on the [Swift Forums](https://forums.swift.org) or other community channels.

## `RuntimeError: memory access out of bounds`

If you encounter this error, there are a few possible causes:

### 1. Invalid memory access in your code

This can happen when using `UnsafePointer` or other unsafe constructs. Review your code for potential memory safety issues.

### 2. Incorrect WASI reactor initialization

If your Wasm module is intended to be used as a library (a “reactor”), it needs to be initialized correctly by the host. Ensure your host environment calls the `_initialize` function if required by the WASI reactor ABI. See the [Exporting a function](./importingexportingfunctions.md) guide for an example.

### 3. Stack overflow

A stack overflow can trigger this error. You have a few options to address this:

- **Avoid deep recursion:** Refactor your code to use an iterative approach if possible.
- **Increase stack size:** You can increase the stack size via a linker option.

  ```bash
  swift build --swift-sdk <SDK_ID> -Xlinker -z -Xlinker stack-size=131072
  ```

## `fatal error: 'stdlib.h' file not found`

This error indicates that the compiler cannot find the necessary C standard library headers for the target platform. Ensure you are using the `--swift-sdk <SDK_ID>` flag with `swift build` to correctly configure the compiler for cross-compilation.

## `error: missing external dependency ...`

You may encounter this error if you are trying to invoke `swiftc` directly. The Swift SDK for WebAssembly currently requires you to build using the Swift Package Manager. Use the `swift build --swift-sdk <SDK_ID>` command instead.

## See Also

- [Porting code from other platforms](./porting.md)
  Make your code cross-platform and compatible with WebAssembly by checking for libraries and APIs available for this platform.
- [Testing](./testing.md)
  Swift for WebAssembly supports both `swift-testing` and `XCTest` for writing test suites. Your project needs to have a `Package.swift` package manifest with test targets configured.
- [Concurrency](./concurrency.md)
  On macOS, iOS, and Linux, the `libdispatch`-based executor is used by default, but `libdispatch` is not supported in a single-threaded WebAssembly environment. However, there are still two global task executors available in Swift for Wasm.
- [Debugging](./debugging.md)
  Debugging is a crucial part of the development process. With official toolchains providing more integrated tools, debugging WebAssembly modules has become more streamlined.
- [Importing and Exporting Functions](./importingexportingfunctions.md)
  WebAssembly modules often need to interact with their host environment. This guide demonstrates how to build a Swift guest module that both exports functions to the host and imports functions from it, using `WasmKit` as the host application.
- [Multi-threading](./multithreading.md)
  While Swift Concurrency is available in Swift for WebAssembly out of the box, it is single-threaded by default. Read this article for special considerations relevant to multi-threading.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/wasmguide/troubleshooting)*