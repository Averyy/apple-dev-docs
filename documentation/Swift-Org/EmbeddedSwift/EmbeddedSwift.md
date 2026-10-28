---
url: "https://docs.swift.org/latest/documentation/embeddedswift"
framework: "Swift-Org/EmbeddedSwift"
---

# Embedded Swift

**Framework**: Swift-Org/EmbeddedSwift

Develop baremetal, embedded, and standalone software in Swift using Embedded Swift’s compilation and language mode.

## Overview

Embedded Swift provides a compilation model tailored to microcontrollers and other resource-constrained devices, producing small, freestanding binaries with no hidden runtime costs. The mode eliminates dynamic language features like reflection and runtime type metadata, replacing them with compile-time specialization so that generics, protocols, and other high-level Swift features compile down to code comparable to a traditional C compiler’s output. Embedded Swift also provides full C and C++ interoperability, letting you integrate with existing vendor SDKs and hardware drivers, or write fully baremetal code with no SDK at all.

> **Note**: Embedded Swift is experimental. Public releases of Swift do not support Embedded Swift, yet. See [Installing Embedded Swift](./installembeddedswift.md) for details.

Embedded Swift also retains modern language features such as optionals, generics, and strong type safety, along with support for Unicode-compliant strings, conditional compilation, and library linkage models suited to embedded targets. You can rely on the full safety guarantees of Swift even when targeting devices with as little as kilobytes of available memory.

Embedded Swift is strictly a *subset* of the Swift language, not a separate dialect, so code written for Embedded Swift also compiles and behaves identically in full Swift. This makes it possible to share code between an embedded target and full Swift using conditional compilation, and to prototype or test your logic on macOS or Linux before deploying it to a physical device.

Boards with active community support include the Raspberry Pi Pico, various STM32 development boards, several ESP32 variants, and nRF52840-based boards, with more platforms being regularly added as the community grows. Whichever hardware you target, you can choose between integrating with an existing vendor SDK or writing fully baremetal code for maximum control.

## Topics

### Essentials
- [Introducing Embedded Swift](./introduction.md)
  Write Swift code for microcontrollers, embedded systems, and baremetal applications.
- [Learning the basics of Embedded Swift](./basics.md)
  Get basic information for using Embedded Swift in typical embedded projects.
### Installation and usage
- [Installing Embedded Swift](./installembeddedswift.md)
  Get the tools needed to use Embedded Swift.
- [Examples](./examples.md)
  Explore complete, step-by-step projects for popular embedded platforms.
### Language features
- [Reviewing the language subset](./languagesubset.md)
  Learn about the Embedded Swift language subset compared to full Swift.
- [Using strings](./strings.md)
  Enable full Unicode-compliant string support in Embedded Swift.
- [Conditionalizing compilation for Embedded Swift](./conditionalcompilation.md)
  Share code between Embedded Swift and full Swift using conditional compilation.
- [Using libraries and modules in Embedded Swift](./libraries.md)
  Learn about the library setup and linkage model of Embedded Swift.
- [Managing external dependencies](./externaldependencies.md)
  Learn what external system dependencies to expect from Embedded Swift compilations.
- [Working with existentials](./existentials.md)
  Learn about restrictions on existentials that apply in Embedded Swift.
- [Restricting non-final generic methods](./nonfinalgenericmethods.md)
  Learn why unbound generic methods aren’t allowed in Embedded Swift.
### SDK support
- [Integrating with embedded platforms](./integratingwithplatforms.md)
  Learn the common patterns and approaches for integrating Swift with existing embedded systems.
- [Bringing Embedded Swift to a new platform](./portingtonewplatforms.md)
  Implement the small set of runtime entry points that Embedded Swift expects from any platform, hosted or baremetal.
- [Using Embedded Swift in baremetal mode](./baremetal.md)
  Program without an SDK for maximum control and minimal size.
- [Integrating with the Raspberry Pi Pico SDK](./integratewithpico.md)
  Set up a project that can seamlessly use C APIs from the Pico SDK.
- [Integrating with the Zephyr RTOS SDK](./integratewithzephyr.md)
  Integrate Swift with Zephyr RTOS for embedded systems development.
### Compiler development and details
- [Exploring Embedded Swift’s ABI](./abi.md)
  Learn about the different ABI (Application Binary Interface) for Embedded Swift.
- [Tracking implementation status](./status.md)
  Compare compiler and language feature support in Embedded Swift to standard Swift.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift)*