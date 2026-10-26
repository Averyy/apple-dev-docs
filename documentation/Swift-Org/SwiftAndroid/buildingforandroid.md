---
url: "https://docs.swift.org/latest/documentation/swiftandroid/buildingforandroid"
framework: "Swift-Org/SwiftAndroid"
---

# Building for Android

**Framework**: Swift-Org/SwiftAndroid  
**Role**: Article

Cross-compile Swift code and package it into Android applications

#### Overview

Swift on Android uses cross-compilation: you build on a macOS or Linux host, and the compiler produces native ARM or x86_64 binaries targeting Android.

```shell
$ swift build --swift-sdk aarch64-unknown-linux-android28
```

#### Conditional compilation

Use `#if os(Android)` to conditionalize code for Android:

```swift
#if os(Android)
import Android
#elseif canImport(Darwin)
import Darwin
#endif
```

#### Foundation

Foundation networking types require a separate import on non-Apple platforms:

```swift
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif
```

#### JNI integration

Export Swift functions for JNI using `@_cdecl`:

```swift
@_cdecl("Java_com_example_MyClass_hello")
func hello(env: UnsafeMutablePointer<JNIEnv>, thisObj: jobject) -> jstring {
    return env.pointee.pointee.NewStringUTF(env, "Hello from Swift")!
}
```

## See Also

### Getting Started
- [Getting Started](./gettingstarted.md)
  Install the Swift toolchain, Android NDK, and Swift SDK for Android


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftandroid/buildingforandroid)*