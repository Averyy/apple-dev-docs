---
url: "https://docs.swift.org/latest/documentation/swiftandroid/integration"
framework: "Swift-Org/SwiftAndroid"
---

# Integration

**Framework**: Swift-Org/SwiftAndroid  
**Role**: Article

Integrate Swift builds with Android tooling and frameworks

#### Gradle

Add a custom Gradle task to invoke `swift build` and copy the resulting `.so` into `jniLibs/`:

```kotlin
tasks.register<Exec>("buildSwiftLibrary") {
    workingDir = file("${rootDir}/swift")
    commandLine("swift", "build",
        "--swift-sdk", "aarch64-unknown-linux-android28",
        "-c", "release", "--static-swift-stdlib")
}
```

#### Swift Package Manager

```shell
$ swift build --swift-sdk aarch64-unknown-linux-android28
```

#### Resources

- [Swift SDK for Android – Getting Started](https://www.swift.org/documentation/articles/swift-sdk-for-android-getting-started.html)
- [swift-java](https://github.com/swiftlang/swift-java) – Java/Kotlin interop
- [swift-android-action](https://github.com/marketplace/actions/swift-android-action) – GitHub Actions
- [Swift Forums](https://forums.swift.org/)

## See Also

### Guides
- [Porting Swift Packages to Android](./portingpackages.md)
  Adapt existing Swift packages to build and run on Android


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftandroid/integration)*