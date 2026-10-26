---
url: "https://docs.swift.org/latest/documentation/wasmguide/debugging"
framework: "Swift-Org/WasmGuide"
---

# Debugging

**Framework**: Swift-Org/WasmGuide  
**Role**: Article

Debugging is a crucial part of the development process. With official toolchains providing more integrated tools, debugging WebAssembly modules has become more streamlined.

#### Overview

These tools are DWARF-based, so ensure you build your application with debug information enabled (which is the default for `swift build`).

#### LLDB and WasmKit

For Swift `main` development snapshots, the toolchain includes enhanced support for debugging WebAssembly. The toolchain bundles `WasmKit`, a runtime that can execute Wasm modules, and an LLDB with WebAssembly support.

`WasmKit` provides debugging capabilities through the GDB Remote Protocol. This allows you to use the version of LLDB bundled with the `main` snapshot toolchain to connect to a running `WasmKit` process for in-depth, command-line debugging.

When using the [Swift extension for VS Code](https://marketplace.visualstudio.com/items?itemName=swiftlang.swift-vscode) with a `main` snapshot toolchain, you can get a more integrated experience:

- **Step through code:** Set breakpoints and step through your Swift code directly within the IDE.
- **Inspect state:** View variables, backtraces, and the current state of your application.

#### Debugging in JavaScript environments

If you’re debugging a WebAssembly app that runs in JavaScript environments (browsers or Node.js), please refer to the [JavaScriptKit Debugging documentation](https://swiftpackageindex.com/swiftwasm/javascriptkit/documentation/javascriptkit/debugging) for detailed information on how to use browser developer tools and other JS-specific debugging utilities.

## See Also

- [Porting code from other platforms](./porting.md)
  Make your code cross-platform and compatible with WebAssembly by checking for libraries and APIs available for this platform.
- [Testing](./testing.md)
  Swift for WebAssembly supports both `swift-testing` and `XCTest` for writing test suites. Your project needs to have a `Package.swift` package manifest with test targets configured.
- [Concurrency](./concurrency.md)
  On macOS, iOS, and Linux, the `libdispatch`-based executor is used by default, but `libdispatch` is not supported in a single-threaded WebAssembly environment. However, there are still two global task executors available in Swift for Wasm.
- [Troubleshooting](./troubleshooting.md)
  These are some common issues you may run into while using Swift with WebAssembly.
- [Importing and Exporting Functions](./importingexportingfunctions.md)
  WebAssembly modules often need to interact with their host environment. This guide demonstrates how to build a Swift guest module that both exports functions to the host and imports functions from it, using `WasmKit` as the host application.
- [Multi-threading](./multithreading.md)
  While Swift Concurrency is available in Swift for WebAssembly out of the box, it is single-threaded by default. Read this article for special considerations relevant to multi-threading.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/wasmguide/debugging)*