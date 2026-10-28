---
url: "https://docs.swift.org/latest/documentation/swiftandroid/portingpackages"
framework: "Swift-Org/SwiftAndroid"
---

# Porting Swift Packages to Android

**Framework**: Swift-Org/SwiftAndroid  
**Role**: Article

Adapt existing Swift packages to build and run on Android

## Overview

Many Swift packages build for Android with minimal changes. The typical process is: attempt a build, fix platform-specific code with conditional compilation, then test on a device.

## Good candidates

- Business logic, algorithms, data structures
- Networking and API clients
- Parsers, formatters, encoders/decoders
- SQLite and other database access

## Conditional imports

```swift
#if canImport(Darwin)
import Darwin
#elseif canImport(Android)
import Android
#elseif canImport(Glibc)
import Glibc
#endif
```

## See Also

### Guides
- [Integration](./integration.md)
  Integrate Swift builds with Android tooling and frameworks


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftandroid/portingpackages)*