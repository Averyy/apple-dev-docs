---
url: "https://docs.swift.org/latest/documentation/swiftandroid/gettingstarted"
framework: "Swift-Org/SwiftAndroid"
---

# Getting Started

**Framework**: Swift-Org/SwiftAndroid  
**Role**: Article

Install the Swift toolchain, Android NDK, and Swift SDK for Android

## Overview

Development requires three components:

1. **Swift Toolchain** – install with [swiftly](https://github.com/swiftlang/swiftly): `swiftly install latest`
2. **Android NDK** – download from [developer.android.com](https://developer.android.com/ndk/downloads) (r27d+ recommended)
3. **Swift SDK for Android** – install with `swift sdk install` (see [swift.org](https://www.swift.org/documentation/articles/swift-sdk-for-android-getting-started.html))

## Hello World

```shell
$ swift package init --type executable
$ swift build --swift-sdk aarch64-unknown-linux-android28
$ adb push .build/aarch64-unknown-linux-android28/debug/HelloWorld /data/local/tmp/
$ adb shell /data/local/tmp/HelloWorld
Hello, world!
```

## Target triples

| Architecture | Triple |
| --- | --- |
| ARM64 | `aarch64-unknown-linux-android28` |
| ARM32 | `armv7-unknown-linux-androideabi28` |
| x86_64 | `x86_64-unknown-linux-android28` |

## See Also

### Getting Started
- [Building for Android](./buildingforandroid.md)
  Cross-compile Swift code and package it into Android applications


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftandroid/gettingstarted)*