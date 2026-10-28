---
url: "https://docs.swift.org/latest/documentation/wasmguide"
framework: "Swift-Org/WasmGuide"
---

# WebAssembly (Wasm)

**Framework**: Swift-Org/WasmGuide  
**Kind**: module

Run Swift in the browser and beyond: interoperate with JavaScript and port existing code.

## Overview

For initial setup, building your first application, and editor configuration, please refer to the official [Getting Started with Swift SDKs for WebAssembly](https://www.swift.org/documentation/articles/wasm-getting-started.html) article on Swift.org.

Once you have your environment set up, you can dive into the topics below to learn more about building powerful [WebAssembly](https://webassembly.org) applications with Swift.

## JavaScript Interoperability

Running Swift in the browser is a common use case for WebAssembly. When not using high-level libraries, direct calls to JavaScript from Swift to [Web APIs](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction) or [DOM APIs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) may be necessary.

See the [JavaScriptKit documentation](https://swiftpackageindex.com/swiftwasm/JavaScriptKit/documentation/javascriptkit) for details on how to interact with JavaScript from Swift.

## Topics

- [Porting code from other platforms](./porting.md)
  Make your code cross-platform and compatible with WebAssembly by checking for libraries and APIs available for this platform.
- [Testing](./testing.md)
  Swift for WebAssembly supports both `swift-testing` and `XCTest` for writing test suites. Your project needs to have a `Package.swift` package manifest with test targets configured.
- [Concurrency](./concurrency.md)
  On macOS, iOS, and Linux, the `libdispatch`-based executor is used by default, but `libdispatch` is not supported in a single-threaded WebAssembly environment. However, there are still two global task executors available in Swift for Wasm.
- [Debugging](./debugging.md)
  Debugging is a crucial part of the development process. With official toolchains providing more integrated tools, debugging WebAssembly modules has become more streamlined.
- [Troubleshooting](./troubleshooting.md)
  These are some common issues you may run into while using Swift with WebAssembly.
- [Importing and Exporting Functions](./importingexportingfunctions.md)
  WebAssembly modules often need to interact with their host environment. This guide demonstrates how to build a Swift guest module that both exports functions to the host and imports functions from it, using `WasmKit` as the host application.
- [Multi-threading](./multithreading.md)
  While Swift Concurrency is available in Swift for WebAssembly out of the box, it is single-threaded by default. Read this article for special considerations relevant to multi-threading.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/wasmguide)*